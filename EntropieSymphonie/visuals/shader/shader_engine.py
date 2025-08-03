from PIL import Image, ImageDraw, ImageTk
import colorsys
import math
import random

class ShaderEngine:
    def __init__(self, width=400, height=400, mode="default"):
        self.width = width
        self.height = height
        self.frame = None
        self.time_accumulator = 0.0
        self.particles = []
        self.mode = mode
        self.intensitaet = 1.0  # Bewegung & Effektfrequenzfaktor

    def set_intensitaet(self, value):
        self.intensitaet = max(0.1, min(value, 10.0))  # Begrenzung aus Sicherheitsgründen

    def entropie_to_color(self, value):
        norm = max(0.0, min(value / 5.0, 1.0))
        hue = (1.0 - norm) * 240 / 360
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        return tuple(int(c * 255) for c in rgb)

    def generate_particles(self, entropie_value):
        num_particles = int(entropie_value * 10)
        self.particles.clear()
        for _ in range(num_particles):
            x = random.randint(0, self.width)
            y = random.randint(0, self.height)
            vx = random.uniform(-1, 1) * self.intensitaet
            vy = random.uniform(-1, 1) * self.intensitaet
            self.particles.append({"x": x, "y": y, "vx": vx, "vy": vy})

    def update_particles(self):
        for p in self.particles:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            if p["x"] < 0 or p["x"] > self.width: p["vx"] *= -1
            if p["y"] < 0 or p["y"] > self.height: p["vy"] *= -1

    def render(self, entropie_value):
        color = self.entropie_to_color(entropie_value)
        image = Image.new("RGB", (self.width, self.height), color)
        draw = ImageDraw.Draw(image)

        # Shader-Modi
        if self.mode == "nebel":
            fog_strength = int((math.sin(self.time_accumulator * 2 * self.intensitaet) * 0.5 + 0.5) * 120)
            fog = Image.new("RGBA", (self.width, self.height), (180, 180, 180, fog_strength))
            image = Image.alpha_composite(image.convert("RGBA"), fog).convert("RGB")

        elif self.mode == "flammen":
            flame_intensity = int((math.sin(self.time_accumulator * 8 * self.intensitaet) * 0.5 + 0.5) * 255)
            flame_overlay = Image.new("RGBA", (self.width, self.height), (255, flame_intensity, 0, 100))
            image = Image.alpha_composite(image.convert("RGBA"), flame_overlay).convert("RGB")

        elif self.mode == "chaos":
            noise = Image.new("RGB", (self.width, self.height))
            noise_pixels = noise.load()
            for x in range(self.width):
                for y in range(self.height):
                    r = random.randint(0, 255)
                    g = random.randint(0, 255)
                    b = random.randint(0, 255)
                    noise_pixels[x, y] = (r, g, b)
            image = Image.blend(image, noise, 0.2)

        draw.text((10, 10), f"Entropie: {entropie_value:.2f}", fill=(255, 255, 255))

        if entropie_value > 2.5:
            alpha = int((math.sin(self.time_accumulator * 5 * self.intensitaet) * 0.5 + 0.5) * 180)
            overlay = Image.new("RGBA", (self.width, self.height), (255, 255, 255, alpha))
            image = Image.alpha_composite(image.convert("RGBA"), overlay).convert("RGB")

        if entropie_value > 1.5 and not self.particles:
            self.generate_particles(entropie_value)

        self.update_particles()
        for p in self.particles:
            # Farbgebung nach Richtung & Geschwindigkeit
            speed = math.sqrt(p["vx"]**2 + p["vy"]**2)
            norm_speed = min(speed / (2 * self.intensitaet), 1.0)
            r = int(abs(p["vx"]) * 255 / self.intensitaet)
            g = int(norm_speed * 255)
            b = int(abs(p["vy"]) * 255 / self.intensitaet)
            draw.ellipse([(p["x"] - 2, p["y"] - 2), (p["x"] + 2, p["y"] + 2)], fill=(r, g, b))

        self.frame = ImageTk.PhotoImage(image)
        return self.frame

    def tick(self, delta_time):
        self.time_accumulator += delta_time * self.intensitaet

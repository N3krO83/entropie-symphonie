import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from visuals.shader.shader_engine import ShaderVisualizer
from sound_player import spiele_crescendo

class EntropieGUI:
    def __init__(self, master, entropie_wert):
        self.master = master
        self.entropie_value = entropie_wert
        self.bewegung_intensitaet = 1.0  # Standardwert
        self.shader = ShaderVisualizer()

        self.setup_interface()
        self.tick_loop()

        if self.entropie_value >= 2.0:
            self.play_selected_sound()

    def setup_interface(self):
        self.master.title("EntropieSymphonie 🎶")
        self.master.geometry("800x800")
        self.master.configure(bg="#1A1A1A")

        self.canvas = tk.Canvas(self.master, width=800, height=600)
        self.canvas.pack()

        rahmen = ttk.Frame(self.master)
        rahmen.pack()

        # Entropie
        self.label_entropie = ttk.Label(rahmen, text=f"Berechnete Entropie: {self.entropie_value:.2f}",
                                        foreground="#00CED1", font=("Helvetica", 18, "bold"))
        self.label_entropie.pack(pady=(10, 10))
        self.slider = ttk.Scale(rahmen, from_=0.0, to=5.0, orient="horizontal",
                                command=self.slider_update, length=400)
        self.slider.set(self.entropie_value)
        self.slider.pack()

        # Bewegung / Frequenz Intensität
        ttk.Label(rahmen, text="Bewegungsfrequenz:", font=("Helvetica", 14)).pack(pady=(10, 0))
        self.label_freq = ttk.Label(rahmen, text=f"{self.bewegung_intensitaet:.2f}", font=("Helvetica", 12))
        self.label_freq.pack()
        self.freq_slider = ttk.Scale(rahmen, from_=0.1, to=5.0, orient="horizontal",
                                     command=self.freq_update, length=400)
        self.freq_slider.set(self.bewegung_intensitaet)
        self.freq_slider.pack()

        # Soundauswahl
        ttk.Label(rahmen, text="Wähle deinen Klang:", font=("Helvetica", 14)).pack(pady=(10, 0))
        self.sound_files = [
            "calm-space-music-312291.mp3",
            "interstellar-355703.mp3",
            "interstellar-adventure-space-theme-soundtrack-4494.mp3",
            "interstellar-drip-ii-337275.mp3",
            "oumuamua-341220.mp3",
            "rizzlas-time-224651.mp3"
        ]
        self.selected_sound = tk.StringVar(value=self.sound_files[0])
        ttk.Combobox(rahmen, textvariable=self.selected_sound, values=self.sound_files,
                     state="readonly", width=40).pack(pady=(5, 10))

        ttk.Button(rahmen, text="Sound abspielen 🎧", command=self.play_selected_sound).pack()
        ttk.Button(rahmen, text="Fenster schließen", command=self.master.destroy).pack(pady=10)

    def slider_update(self, val):
        self.set_entropie(float(val))
        self.label_entropie.config(text=f"Berechnete Entropie: {self.entropie_value:.2f}")

    def freq_update(self, val):
        self.bewegung_intensitaet = float(val)
        self.label_freq.config(text=f"{self.bewegung_intensitaet:.2f}")
        if hasattr(self.shader, "set_intensitaet"):
            self.shader.set_intensitaet(self.bewegung_intensitaet)

    def play_selected_sound(self):
        spiele_crescendo(f"sounds/{self.selected_sound.get()}")

    def tick_loop(self):
        self.shader.tick(0.016)
        frame = self.shader.render(self.entropie_value)
        resized = frame.resize((800, 600))
        self.image_obj = ImageTk.PhotoImage(resized)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_obj)
        self.master.after(16, self.tick_loop)

    def set_entropie(self, value):
        self.entropie_value = value

import numpy as np
import matplotlib.pyplot as plt
import json
import time

# 🌀 Modulierte Intensität berechnen
def berechne_modulierte_intensitaet(modulation):
    if modulation.get("aktiv", False):
        t = time.time()
        freq = modulation.get("frequenz", 0.2)
        amp = modulation.get("amplitude", 1.0)
        offset = modulation.get("offset", 0.5)
        chaos = modulation.get("chaos", 0.0)

        puls = amp * np.sin(freq * t) + offset
        noise = np.random.uniform(-chaos, chaos)
        return max(0.1, puls + noise)
    else:
        return 1.0

# ⚛️ Teilchenschwingung visualisieren
def zeichne_quanten_partikel(n=50, entropie=0.5, pfad="visuals/teilchenschwingung.png"):
    """
    Visualisiert quantenartige Teilchen mit zufälliger Bewegung.
    Farbe & Größe werden durch Frequenz & Trigger moduliert.
    """

    # 📥 Triggerdaten laden
    try:
        with open("data/gegenwart_trigger.json", "r") as f:
            daten = json.load(f)
        trigger_aktiviert = daten.get("trigger", False)
        modulation = daten.get("modulation", {})
        max_intensitaet = berechne_modulierte_intensitaet(modulation)
    except FileNotFoundError:
        trigger_aktiviert = False
        max_intensitaet = 1.0

    # 🎲 Zufällige Positionen
    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)

    # 🔉 Frequenzberechnung
    frequenz = np.random.uniform(0.5, 2.0, n)
    energie = np.abs(np.sin(frequenz * np.pi * entropie))

    # 🎨 Farbe bestimmen
    farben = []
    for f in frequenz:
        if trigger_aktiviert:
            farben.append("deepskyblue" if f > 1.0 else "gainsboro")
        else:
            if f > 1.5:
                farben.append("orchid")
            elif f < 0.8:
                farben.append("palegreen")
            else:
                farben.append("khaki")

    # 📊 Plot erstellen
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(
        x, y, 
        s=(energie * 100 + 30) * max_intensitaet,
        c=farben, alpha=0.8, edgecolors="white", linewidths=0.5
    )

    ax.set_title("⚛️ Teilchenschwingung mit lebendiger Modulation", fontsize=13)
    ax.set_xlabel("Horizontale Bewusstseinsachse")
    ax.set_ylabel("Vertikale Resonanzachse")
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.grid(True, linestyle="--", alpha=0.2)
    ax.set_facecolor("black")

    plt.tight_layout()
    plt.savefig(pfad, dpi=120)
    plt.close()
    print(f"✅ Visualisierung gespeichert unter: {pfad}")


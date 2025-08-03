import numpy as np
import matplotlib.pyplot as plt

def zeichne_gedankenfelder(p=0.5, i=0.5, v=0.5, f=0.5, pfad="visuals/gedankenfeld.png"):
    """
    Erstellt eine Vektorwolke zur symbolischen Darstellung kollektiver Gedankenbewegung.
    
    Parameter:
    - p: Polarisierung (0–1)
    - i: Informationschaos (0–1)
    - v: Vertrauensverlust (0–1)
    - f: Fragmentierung (0–1)
    - pfad: Speicherort der erzeugten PNG-Datei
    """

    # 🔣 Raster für die Vektorfelder (10x10 Gitterpunkte)
    x, y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))

    # 📐 Berechne Vektorrichtungen basierend auf Parametern
    u = np.sin(np.pi * x * p) + f * y
    v_vec = np.cos(np.pi * y * i) - v * x

    # 🎨 Plot erstellen
    fig, ax = plt.subplots(figsize=(6, 6))
    q = ax.quiver(x, y, u, v_vec, color="navy", scale=5)

    # ♿ Barrierefreiheit: klare Achsen, hoher Kontrast, Titel
    ax.set_title("🧠 Gedankenfeld-Vektoren", fontsize=14)
    ax.set_xlabel("Kognitive Ausrichtung")
    ax.set_ylabel("Emotionale Dichte")
    ax.set_xticks(np.linspace(-1, 1, 5))
    ax.set_yticks(np.linspace(-1, 1, 5))
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.3)

    # 📦 Layout & Speichern
    plt.tight_layout()
    plt.savefig(pfad, dpi=120)
    plt.close()
    print(f"✅ Gedankenfeld gespeichert unter: {pfad}")

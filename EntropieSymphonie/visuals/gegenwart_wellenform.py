import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# 🖼️ Funktion zur Bildüberlagerung
def überlagere_silhouette(ax, emotionale_präsenz, schwelle=0.8):
    if emotionale_präsenz >= schwelle:
        silhouette = mpimg.imread("assets/silhouette.png")
        ax.imshow(
            silhouette,
            extent=[-0.5, 0.5, -0.5, 0.5],
            alpha=0.4
        )

# 🌑 Funktion zur Annotation
def zeichne_annotierte_präsenz(ax, emotionale_präsenz, schwelle=0.8):
    if emotionale_präsenz >= schwelle:
        ax.annotate(
            "🌑 Silhouette aktiv",
            xy=(0.5, 0.5),
            xycoords='axes fraction',
            fontsize=12,
            color="white",
            ha="center"
        )

# 🧠 Simulierter Präsenzwert (z. B. aus Frequenzdaten berechnet)
def berechne_emotionale_präsenz(frequenzdaten):
    # Beispiel: Präsenz steigt mit mittlerer Frequenzintensität
    return np.clip(np.mean(np.abs(frequenzdaten)), 0, 1)

# 🌀 Hauptfunktion zur Wellenformdarstellung
def zeichne_gegenwart_wellenform(frequenzdaten, pfad="visuals/wellenform.png"):
    emotionale_präsenz = berechne_emotionale_präsenz(frequenzdaten)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(frequenzdaten, color="cyan", linewidth=2)

    # Schwellenintegration
    überlagere_silhouette(ax, emotionale_präsenz)
    zeichne_annotierte_präsenz(ax, emotionale_präsenz)

    ax.set_title("🫧 Frequenzwellenform der Gegenwart", fontsize=13)
    ax.set_xlabel("Zeit")
    ax.set_ylabel("Intensität")
    ax.grid(True, linestyle="--", alpha=0.3)
    ax.set_facecolor("black")

    plt.tight_layout()
    plt.savefig(pfad, dpi=120)
    plt.close()
    print(f"✅ Wellenform gespeichert unter: {pfad}")

# 🧪 Beispiel-Daten & Testaufruf
if __name__ == "__main__":
    beispiel_frequenz = np.sin(np.linspace(0, 6 * np.pi, 100)) * np.random.uniform(0.8, 1.2, 100)
    zeichne_gegenwart_wellenform(beispiel_frequenz)

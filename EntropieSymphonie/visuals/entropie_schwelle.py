import matplotlib.pyplot as plt

def entropie_und_schwelle_plot(entropie, schwelle=0.75, pfad="visuals/entropie_schwelle.png"):
    # 🔧 Erzeuge eine neue Plot-Figur mit definierter Größe
    fig, ax = plt.subplots(figsize=(6, 3))
    
    # 📦 Werte und Labels für die Balken
    werte = [entropie, schwelle]
    labels = ["Aktuelle Entropie", "Schwellenwert"]
    
    # 🎨 Farbwahl: Rot bei Überschreitung, Grün sonst, Schwelle in Grau
    farben = ["crimson" if entropie > schwelle else "green", "gray"]

    # 📊 Erzeuge den Balkenplot
    ax.bar(labels, werte, color=farben)
    ax.set_ylim(0, 1)                    # ⚙️ Y-Achse von 0 bis 1
    ax.set_ylabel("Entropiewert")        # 📝 Achsenbeschriftung
    ax.set_title("🧠 Entropie & Schwellenwertvergleich")  # 🏷️ Titel des Plots

    # 🔢 Werte als Text über den Balken anzeigen
    for i, v in enumerate(werte):
        ax.text(i, v + 0.02, f"{v:.2f}", ha='center', va='bottom')

    # 📦 Layout anpassen & speichern
    plt.tight_layout()
    plt.savefig(pfad)
    plt.close()  # 🚪 Plot schließen, um Speicher freizugeben
    print(f"✅ Entropie-Schwellenwert-Plot gespeichert unter: {pfad}")

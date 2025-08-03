import numpy as np
import time
from gegenwart_wellenform import zeichne_gegenwart_wellenform, berechne_emotionale_präsenz
from teilchen_schwingung import zeichne_quanten_partikel

# 🎛️ Frequenzdaten simulieren
def generiere_frequenzdaten(n=100):
    t = np.linspace(0, 6 * np.pi, n)
    modulation = np.sin(t) * np.random.uniform(0.6, 1.3, n)
    return modulation

# 🔁 Hauptsynchronisationsfunktion
def synchronisiere_visualisierungen():
    # 1️⃣ Frequenzdaten generieren
    frequenzdaten = generiere_frequenzdaten()

    # 2️⃣ Präsenz berechnen
    emotionale_präsenz = berechne_emotionale_präsenz(frequenzdaten)

    # 3️⃣ Triggerdatei aktualisieren
    daten = {
        "trigger": True,
        "modulation": {
            "aktiv": True,
            "frequenz": 0.2,
            "amplitude": 1.2,
            "offset": 0.6,
            "chaos": 0.25
        }
    }

    # 🧾 In JSON speichern
    import json
    with open("data/gegenwart_trigger.json", "w") as f:
        json.dump(daten, f, indent=2)

    # 4️⃣ Visualisierungen auslösen
    zeichne_gegenwart_wellenform(frequenzdaten)
    zeichne_quanten_partikel(n=80, entropie=emotionale_präsenz)

    print("✅ Synchronisierte Visualisierung abgeschlossen.")

# 🧪 Testlauf
if __name__ == "__main__":
    synchronisiere_visualisierungen()

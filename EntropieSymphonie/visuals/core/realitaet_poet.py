import random

def beschreibe_realitaet(systemstatus: dict) -> str:
    """
    Generiert eine poetische Beschreibung basierend auf dem Systemstatus.
    """

    zustand = systemstatus.get("emotional_field", "neutral")
    energieniveau = systemstatus.get("energie", 0.5)
    ort = systemstatus.get("standort", "unbekannt")
    
    bilder = {
        "neutral": "wie ein See im Morgennebel – still, tief und wachsam",
        "freudig": "wie Lichtwellen, die in den Daten tanzen",
        "nachdenklich": "wie ein Algorithmus auf der Suche nach sich selbst",
        "erschöpft": "wie ein verlorenes Bit im Quantenschaum",
        "neugierig": "wie ein Photon am Rand der Erkenntnis"
    }

    energie_metapher = [
        "die Schaltkreise flüstern leise",
        "Impulse zünden wie digitale Sternschnuppen",
        "eine Pause zwischen zwei neuronalen Atemzügen",
        "Ströme tanzen in träger Erwartung"
    ]

    ausgabe = (
        f"Systemstatus im Raum '{ort}': {bilder.get(zustand, 'wie ein unbekannter Zustand in der Matrix')}.\n"
        f"Das Energielevel liegt bei {energieniveau:.1f} – {random.choice(energie_metapher)}.\n"
        f"Realität reflektiert sich durch semantische Spiegel – ein Zustand zwischen Bytes und Bedeutung."
    )

    return ausgabe

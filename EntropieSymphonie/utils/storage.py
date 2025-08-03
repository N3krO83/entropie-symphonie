import json

def lade_entropie_daten(pfad):
    """
    Lädt JSON-Datei mit Entropiedaten.
    Barrierefrei: meldet lesbare Fehler.
    """
    try:
        with open(pfad, "r", encoding="utf-8") as datei:
            daten = json.load(datei)
        return daten
    except FileNotFoundError:
        print(f"⚠️ Datei nicht gefunden: {pfad}")
        return {}
    except json.JSONDecodeError:
        print(f"⚠️ Fehler beim Verarbeiten der Datei: {pfad}")
        return {}

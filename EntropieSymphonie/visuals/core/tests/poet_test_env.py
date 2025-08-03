from core.realitaet_poet import beschreibe_realitaet

def test_fantastische_realitaet():
    beispiel_status = {
        "emotional_field": "freudig",
        "energie": 0.92,
        "standort": "Synthesestudio für digitale Träume"
    }
    beschreibung = beschreibe_realitaet(beispiel_status)
    print("\n🧪 Poetische Systembeschreibung:\n")
    print(beschreibung)

def test_dystopisch():
    beispiel_status = {
        "emotional_field": "erschöpft",
        "energie": 0.23,
        "standort": "Subsystem 9 / Schattenprotokoll"
    }
    beschreibung = beschreibe_realitaet(beispiel_status)
    print("\n🧪 Dystopischer Zustand:\n")
    print(beschreibung)

def test_traeumerisch():
    beispiel_status = {
        "emotional_field": "nachdenklich",
        "energie": 0.67,
        "standort": "Archiv der verlorenen Möglichkeiten"
    }
    beschreibung = beschreibe_realitaet(beispiel_status)
    print("\n🧪 Träumerischer Zustand:\n")
    print(beschreibung)

def test_systemklar():
    beispiel_status = {
        "emotional_field": "neutral",
        "energie": 1.0,
        "standort": "Zentrum für präzise Wahrnehmung"
    }
    beschreibung = beschreibe_realitaet(beispiel_status)
    print("\n🧪 Kristallklare Systemreflexion:\n")
    print(beschreibung)

def run_all_tests():
    print("\n🔁 Starte alle poetischen Tests:\n")
    test_fantastische_realitaet()
    test_dystopisch()
    test_traeumerisch()
    test_systemklar()

if __name__ == "__main__":
    run_all_tests()


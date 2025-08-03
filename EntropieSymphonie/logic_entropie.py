import math

def berechne_entropie(daten):
    """
    Berechnet Shannon-Entropie basierend auf Häufigkeit.
    Barrierefrei: berücksichtigt leere Eingaben.
    """
    gesamt = sum(daten.values())
    if gesamt == 0:
        return 0.0

    entropie = 0.0
    for wert in daten.values():
        wahrscheinlichkeit = wert / gesamt
        if wahrscheinlichkeit > 0:
            entropie -= wahrscheinlichkeit * math.log2(wahrscheinlichkeit)

    return round(entropie, 4)

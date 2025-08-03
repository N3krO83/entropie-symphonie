import pygame

def lade_sound(pfad):
    """
    Lädt Sound mit Pygame-Mixer.
    Barrierefrei: gibt klare Hinweise bei Fehlern.
    """
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(pfad)
        pygame.mixer.music.set_volume(0.7)
    except Exception as e:
        print("🎵 Fehler beim Laden des Sounds:", e)

def spiele_crescendo(pfad):
    """
    Spielt Sound synchron ab.
    Ideal für taktile Rückmeldung bei hohem Entropiewert.
    """
    lade_sound(pfad)
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print("🎵 Fehler beim Abspielen:", e)

import sys
import tkinter as tk

# 🔧 Eigene Module
from logic_entropie import berechne_entropie
from shader_engine.py import ShaderVisualizer
from utils.storage import lade_entropie_daten
from gui_entropie import EntropieGUI
from core.emotional_field import get_current_entropy
from entropie_analyzer import EntropieAnalyzer  # ← Stelle sicher, dass dieses Modul korrekt vorhanden ist!

def simulation_tick(gui, root):
    """⏱ Aktualisiert Entropie regelmäßig und löst ggf. Sound aus"""
    neuer_wert = get_current_entropy()
    gui.set_entropie(neuer_wert)

    if neuer_wert >= 2.0:
        gui.play_selected_sound()

    root.after(500, lambda: simulation_tick(gui, root))  # alle 0.5 Sekunden

def run_entropie_analyse_test():
    """🧪 Diagnosetest für EntropieAnalyzer"""
    analyzer = EntropieAnalyzer()
    sample = "Die Realität beginnt zu flimmern. Gedanken tanzen am Rand der Ordnung."

    wert, zustand = analyzer.analyze_text(sample)
    beschreibung = analyzer.classify_mood(zustand)

    print(f"\n🧠 Analyse-Test:")
    print(f"Text: {sample}")
    print(f"Entropie-Wert: {wert}")
    print(f"Zustand: {zustand} → {beschreibung}")

def main():
    print("🚀 EntropieSymphonie wird gestartet...")
    print("✅ Starte Imports...")
    print("🧠 Aktiver Python:", sys.executable)

    daten = lade_entropie_daten("data/entropie_export.json")
    initial_entropie = berechne_entropie(daten)

    root = tk.Tk()
    gui = EntropieGUI(root, entropie_wert=initial_entropie)

    simulation_tick(gui, root)
    run_entropie_analyse_test()

    root.mainloop()

if __name__ == "__main__":
    main()

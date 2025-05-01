import pandas as pd
import random
from colorama import Fore, Style, init

# Initialisieren von colorama
init(autoreset=True)

def vokabel_trainer():
    
    print("Willkommen zum Vokabeltrainer!")
    print("Tippe 'exit', um das Programm zu beenden.")
    
    # Dateipfad abfragen
    dateipfad = input("Dateipfad zur Excel-Datei mit den Vokabeln: ")

    # Excel-Datei laden
    try:
        daten = pd.read_excel(dateipfad)
    except FileNotFoundError:
        print(Fore.RED + "Error: Datei " + dateipfad + " wurde nicht gefunden.")
        return
    except Exception as e:
        print(Fore.RED + "Error: Fehler beim Laden der Datei: " + e)
        return

    # Wörterbuch aus Excel-Tabelle erstellen
    try:
        vokabeln = {row['Englisch']: row['Deutsch'] for _, row in daten.iterrows()}
    except KeyError:
        print(Fore.RED + "Error: Die Excel-Datei muss zwei Spalten mit den Namen 'Englisch' und 'Deutsch' enthalten.")
        return

    # Gewichtete Liste, um falsche Wörter häufiger abzufragen
    gewichtete_liste = list(vokabeln.keys())
    letzter_begriff = None

    while True:
        # Zufällige Vokabel aus gewichteter Liste auswählen
        while True:
            englisches_wort = random.choice(gewichtete_liste)
            if englisches_wort != letzter_begriff:
                break
        
        deutsches_wort = vokabeln[englisches_wort]

        # Abfrage
        antwort = input("Was heißt " + Fore.YELLOW + Style.BRIGHT + deutsches_wort + Fore.RESET + Style.NORMAL + " auf Englisch? " + Style.BRIGHT)

        # Programm beenden
        if antwort.lower() == "exit" or antwort.lower() == "Exit":
            print(Style.NORMAL + Fore.YELLOW + "Vokabeltrainer beendet")
            break

        # Überprüfung der Antwort
        if antwort.lower() == englisches_wort.lower():
            print(Fore.GREEN + "Richtig! Gut gemacht!")
            if gewichtete_liste.count(englisches_wort) > 1:
                gewichtete_liste.remove(englisches_wort)
        else:
            print(Fore.RED + "Falsch. Die richtige Antwort ist " + Style.BRIGHT + "'" + englisches_wort + "'")
            gewichtete_liste.extend([englisches_wort] * 15)
            
        letzter_begriff = englisches_wort

# Programm starten
vokabel_trainer()

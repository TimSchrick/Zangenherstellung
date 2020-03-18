# Erstellt von marcelarmin am 18.03.2020 im Rahmen der Python II Schulung
"""
Meine Maschine nimmt das Objekt Zange entgegen und bearbeitet dieses.
Es werden folgende Merkmale an der Zange geschaffen:
- tellern des Gewerbes
- fräsen der Bohrung
- versenken der Bohrung

erwarteter input vom typ:
    class Zange:
        def __init__(self):
            self.erhitzt = False
            self. gebogen = False
            self.geschmiedet = False
            self.abgegratet = False
            self.getellert = False
            self.versenkt = False
            self.gebohrt = False
            self.geoelt = False
            self.vormontiert = False
            self.vernietet = False
            self.geoeffnet = False
            self.eingestellt = False
            self.geprueft = False
"""
from Zange import Zange

def BTV_bearbeitung(schenkel:Zange):
    if type(schenkel) != Zange:
        return print("Eingelegtes Teil ist nicht vom Typ Zange")
    schenkel.getellert = True
    schenkel.versenkt = True
    schenkel.gebohrt = True

    return schenkel

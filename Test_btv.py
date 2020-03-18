"""
IMPORT:
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
import btv
from Zange import Zange

def Test_anlieferung(schenkel:Zange):
    """
    Hiermit teste ich den Anlieferungszustand für die Maschine/Funktion "btv"
    :param schenkel:
    :return: True --> anliefrungszusatnd richtig
    False --> Eins der Merkmale die hier bearbeitet wird ist nicht richtig oder schon bearbeitet
    """
    if schenkel.getellert == False and schenkel.versenkt == False and schenkel.gebohrt == False:
        return True
    else:
        return False

def Test_auslieferung(schenkel:Zange):
    """
    Hiermit teste ich die Funktion (die Maschine) "btv"
    :param schenkel:
    :return: True --> Auslieferung richtig
    False --> Auslieferung falsch
    """
    if schenkel.getellert == True and schenkel.versenkt == True and schenkel.gebohrt == True:
        return True
    else:
        return False
def Test_btv():
    teil = Zange()

    if Test_anlieferung(teil) == True:
        teil = btv.BTV_bearbeitung(teil)
        if Test_auslieferung(teil) == True:
            return True
    else:
        return False

# ------btv_test--------
if Test_btv() == True:
    print("btv funktioniert")

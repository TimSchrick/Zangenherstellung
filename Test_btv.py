import btv
from Zange import Zange

def test_btv():
    "arrange:"
    schenkel = Zange()
    testergebnis = False

    "act:"
    # Hiermit teste ich den Anlieferungszustand für die Maschine/Funktion "btv"
    if schenkel.getellert == False and schenkel.versenkt == False and schenkel.gebohrt == False:
        # Zange bearbeiten
        schenkel = btv.BTV_bearbeitung(schenkel)
        # Hiermit teste ich die Funktion (die Maschine) "btv"
        if schenkel.getellert == True and schenkel.versenkt == True and schenkel.gebohrt == True:
            testergebnis = True

    "assert:"
    assert testergebnis


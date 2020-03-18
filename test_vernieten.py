from Zange import Zange
from Vernieten import oelen, vormontieren, nieten

def test_nietprozess():
    zange = Zange

    # Schmiede Parameter setzen
    zange.erhitzt = True
    zange.gebogen = True
    zange.geschmiedet = True
    zange.abgegratet = True

    # Gewerbe fertigen Parameter setzen
    zange.getellert = True
    zange.versenkt = True
    zange.gebohrt = True

    #oelen
    oelen(zange)
    assert zange.geoelt

    #Vormontieren
    vormontieren(zange)
    assert zange.vormontiert

    # Vernieten
    nieten(zange)
    assert zange.vernietet


test_nietprozess()
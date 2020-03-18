from Zange import Zange
from Vernieten import Nietprozess

def test_nietprozess():
    zange = Zange()
    nm = Nietprozess()

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
    nm.oelen(zange)
    assert zange.geoelt

    #Vormontieren
    nm.vormontieren(zange)
    assert zange.vormontiert

    # Vernieten
    nm.nieten(zange)
    assert zange.vernietet

test_nietprozess()
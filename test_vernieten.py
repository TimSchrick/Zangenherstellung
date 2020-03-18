from Zange import Zange
from Vernieten import Nietprozess

def test_nietprozess():
    zange = Zange()

    # Schmiede Parameter setzen
    zange.erhitzt = True
    zange.gebogen = True
    zange.geschmiedet = True
    zange.abgegratet = True

    # Gewerbe fertigen Parameter setzen
    zange.getellert = True
    zange.versenkt = True
    zange.gebohrt = True

    nm = Nietprozess(zange)

    #oelen
    nm.oelen()
    assert nm.zange.geoelt

    #Vormontieren
    nm.vormontieren()
    assert nm.zange.vormontiert

    # Vernieten
    nm.nieten()
    assert nm.zange.vernietet
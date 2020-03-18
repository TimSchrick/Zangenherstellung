
from Gangeinstellen import Gangeinstellen as GE
from Zange import Zange



def test_oeffnen():
    zange = Zange()
    pG = GE(zange)
    pG.oeffnen()
    assert zange.geoeffnet == True

def test_einstellen():
    zange = Zange()
    pG = GE(zange)
    pG.einstellen()
    assert zange.eingestellt == True

def test_pruefen():
    zange = Zange()
    pG = GE(zange)
    pG.pruefen()
    assert zange.geprueft == True


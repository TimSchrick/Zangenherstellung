
from Gangeinstellen import Gangeinstellen
from Zange import Zange


if __name__ == '__main__':

    zange = Zange()
    pG = Gangeinstellen(zange)
    zange = pG.getresult()
    print(zange.geoeffnet)
    pG = GE(zange)
    zange = pG.dotitandreturn()

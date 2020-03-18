
from Gangeinstellen import Gangeinstellen
from Zange import Zange


if __name__ == '__main__':

    zange = Zange()
    pG = Gangeinstellen(zange)
    zange = pG.dotitandreturn()
    print(zange.geoeffnet)

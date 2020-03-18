
from Gangeinstellen import Gangeinstellen as GE
from Zange import Zange


if __name__ == '__main__':

    zange = Zange()
    pG = GE(zange)
    zange = pG.getresult()
    print()

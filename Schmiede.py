from Zange import Zange
import time

class Piller():
    def __init__(self):
        self.erhitzt = False
        self.gebogen = False
        self.vorgeschmiedet = False


class Schmiede():
    """Hier werden Zangen geboren
    """

    def __init__(self):
        pass

    def prozess(self) -> Zange:
        """Durchläuft den Schmiedeprozess. Schneiden, erhitzen, biegen, schmieden und abgraten.

        Returns:
        --------
        Zange
            Ein Zangenrohling
        """


        p = self.schneiden()
        self.erhitzen(p)
        self.biegen(p)
        z = self.schmieden(p)
        self.abgraten(z)
        return z

    def schneiden(self) -> Piller:
        return Piller()

    def erhitzen(self, piller:Piller) -> Piller:
        print("Erhitze Piller...")
        time.sleep(3)
        piller.erhitzt = True
        print("fertig")
        return piller

    def biegen(self, piller:Piller):
        assert piller.erhitzt

        print("Biege Piller...")
        time.sleep(1)
        piller.gebogen = True
        print("fertig")

        return piller

    def schmieden(self, piller:Piller) -> Zange:
        assert piller.erhitzt
        assert piller.gebogen

        print("Schmiede Zange aus Piller...")
        piller.geschmiedet = True
        
        zange=Zange()
        zange.erhitzt = piller.erhitzt
        zange.gebogen = piller.gebogen
        zange.geschmiedet = True
        print("fertig")
        return zange

    def abgraten(self, zange:Zange) -> Zange:
        assert zange.geschmiedet

        print("Zange wird abgegratet...")
        time.sleep(1)
        zange.abgegratet = True
        print("fertig")

        return zange

s = Schmiede()
z = s.prozess()
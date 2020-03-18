import Zange

class Nietprozess:
    def __init__(self, rohteil):
        """
        :param rohteil: Zangenobjekt
        """
        self.zange = rohteil

    def oelen(self):
        """
        Die Zange wird geölt
        """
        self.zange.geoelt = True

    def vormontieren(self):
        """
        Die Zange wird montiert
        """
        self.zange.vormontiert = True

    def nieten(self):
        """
        Die Zange wird vernietet
        """
        self.zange.vernietet = True
import Zange

class Nietprozess:
    def oelen(self, zange):
        """
        Die Zange wird geölt

        :param zange: Zangenobjekt
        :return: null
        """
        zange.geoelt = True

    def vormontieren(self, zange):
        """
        Die Zange wird montiert

        :param zange: Zangenobjekt
        :return:
        """
        zange.vormontiert = True

    def nieten(self, zange):
        """
        Die Zange wird vernietet

        :param zange: Zangenobjekt
        :return:
        """
        zange.vernietet = True
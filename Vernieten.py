import Zange

class Nietprozess:
    def oelen(zange):
        """
        Die Zange wird geölt

        :param zange: Zangenobjekt
        :return: null
        """
        zange.geoelt = True

    def vormontieren(zange):
        """
        Die Zange wird montiert

        :param zange: Zangenobjekt
        :return:
        """
        zange.vormontiert = True

    def nieten(zange):
        """
        Die Zange wird vernietet

        :param zange: Zangenobjekt
        :return:
        """
        zange.vernietet = True

    def ablauf(zange):
        """
        Der Prozessablauf
        :param zange: Zangenobjekt
        :return:
        """
        oelen(zange)
        vormontieren(zange)
        nieten(zange)
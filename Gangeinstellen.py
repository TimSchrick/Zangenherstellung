

class Gangeinstellen:

    def __init__(self, zange):
        self.zange_obj = zange
        self.doit()

    def oeffnen(self):
        self.zange_obj.geoeffnet = True

    def einstellen(self):
        self.zange_obj.eingestellt = True

    def pruefen(self):
        self.zange_obj.geprueft = True

    def doit(self):
        self.oeffnen()
        self.einstellen()
        self.pruefen()

    def getresult(self):
        return self.zange_obj
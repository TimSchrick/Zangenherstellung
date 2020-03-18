

class Gangeinstellen:

    def __init__(self, zange):
        self.zange_obj = zange

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

    def dotitandreturn(self):
        self.doit()
        return self.zange_obj
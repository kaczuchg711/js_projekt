from klienci.Klient import Klient


class KlientZwykly(Klient):
    def __init__(self,kind):
        super(KlientZwykly,self).__init__(kind)
        self.x = 1
    def __str__(self):
        return KlientZwykly.__name__+ ' ' + super(KlientZwykly,self).__str__()
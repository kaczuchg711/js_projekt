from klienci.Klient import Klient


class KlientZwykly(Klient):
    def __init__(self,kind):
        super(KlientZwykly,self).__init__(kind)

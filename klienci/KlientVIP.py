from klienci.Klient import Klient

class KlientVIP(Klient):
    def __init__(self, kind):
        super(KlientZwykly, self).__init__(kind)
from klienci.Klient import Klient

class KlientVIP(Klient):
    def __init__(self, kind):
        super(KlientZwykly, self).__init__(kind)

    def __str__(self):
        return KlientVIP.__name__+ ' ' + super(KlientZwykly,self).__str__()
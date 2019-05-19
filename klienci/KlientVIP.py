from klienci.Klient import Klient

class KlientVIP(Klient):
    def __init__(self, kind):
        super(KlientVIP, self).__init__(kind)
        self._was_cry = False
        self._sec = 0
    def __str__(self):
        return KlientVIP.__name__+ ' ' + super(KlientVIP,self).__str__()

    def tick(self):
        self.sec += 1
        if self.sec == 10:
            print("to skandaliczne")
            self.sec = 0

    @property
    def was_cry(self):
        return self._was_cry

    @was_cry.setter
    def was_cry(self,tf):
        self._was_cry = tf

    @property
    def sec(self):
        return self._sec

    @sec.setter
    def sec(self,s):
        self._sec = s


import time


class Klient:
    def __init__(self, kind):
        self._kind = kind
        self._waiting_time = 0

    def __del__(self):
        pass

    def __str__(self):
        return 'typ:'+self._kind

    @property
    def waiting_time(self):
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self,wt):
        self._waiting_time = wt

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, kind):
        self._kind = kind

    def wejscie(self):
        self._waiting_time = time.clock_gettime(0)

    def wyjscie(self):
        self._waiting_time = time.clock_gettime(0) - self._waiting_time + 3
        return self._waiting_time

    def tick(self):
        pass

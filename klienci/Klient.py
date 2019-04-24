import time


class Klient:
    def __init__(self, kind):
        self._kind = kind
        self._waiting_time = 0
        self.wejscie()

    def __del__(self):
        self.wyjscie()

    def __str__(self):
        return self._kind

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, kind):
        self._kind = kind

    def wejscie(self):
        self._waiting_time = time.clock_gettime(0)

    def wyjscie(self):
        self._waiting_time = time.clock_gettime(0) - self._waiting_time
        print(self._waiting_time)

    def tick(self):
        pass

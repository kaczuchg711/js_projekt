from klienci.KlientVIP import *

class myQueue():
    def __init__(self, napis):
        self._tab = []
        self._num = 0
        self._napis = napis
        self._i = 0

    def pop(self):
        self.num -= 1
        x = self.tab.pop(0)
        return x

    def get_first(self):
        return self.tab[0]

    def push(self, x):
        x.wejscie()
        self.num += 1
        self.tab.append(x)

    def __str__(self):
        return [x.__str__() for x in self.tab].__str__()

    def __iter__(self):
        return self

    def empty(self):
        print(self.tab.__len__())
        if (self.tab.__len__() == 0):
            return True
        else:
            return False

    def __next__(self):
        if (self.i == self.num):
            self.i = 0
            raise StopIteration
        else:
            self.i += 1
            return self.tab[self.i-1]


    # gs

    @property
    def tab(self):
        return self._tab

    @tab.setter
    def tab(self, tab):
        self._tab = tab

    @property
    def i(self):
        return self._i

    @i.setter
    def i(self, i):
        self._i = i

    @property
    def num(self):
        return self._num

    @num.setter
    def num(self, num):
        self._num = num

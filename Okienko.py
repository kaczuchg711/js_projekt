class Window:
    def __init__(self, n, a=False, b=False):
        self._nr = n
        self._a = a
        self._b = b

    @property
    def nr(self):
        return self._nr

    @nr.setter
    def nr(self, nr):
        self._nr = nr

    @property  # print(w.a)
    def a(self):
        return self._a

    @a.setter  # w.a=True
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b


w = Window(1, True, False)
print(w.a)
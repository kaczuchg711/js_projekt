class Window:
    nr_set = set()

    def __init__(self, n, a=False, b=False):
        """init and add window number in nr_set"""
        if n in Window.nr_set:
            raise ValueError
        else:
            Window.nr_set.add(n)
            self._nr = n
            self._a = a
            self._b = b

    def __del__(self):
        """remove window number in nr_set"""
        Window.nr_set.remove(self._nr)

    @property
    def a(self):
        return self._a

    @property
    def nr(self):
        return self._nr

    @a.setter  # w.a=True
    def a(self, a):
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._b = b

    def __str__(self) -> str:
        return "Window nr: " + str(self.nr) + "a: " + str(self.a) + " b: " + str(self.b)

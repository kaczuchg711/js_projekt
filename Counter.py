class Counter:
    nr_set = set()

    def __init__(self, n, a=False, b=False):
        """init and add window number in nr_set"""
        if n in Counter.nr_set:
            raise ValueError
        else:
            Counter.nr_set.add(n)
            self._nr = n
            self._a = a
            self._b = b
            self._free = True
    def __del__(self):
        """remove window number in nr_set"""
        Counter.nr_set.remove(self._nr)

    @property
    def free(self):
        return self._nr

    @free.setter
    def free(self, ft):
        self._free = ft

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

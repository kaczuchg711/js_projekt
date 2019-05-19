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
            self._client_in = 0
            self._is_measure_time = False
            self._start_time = 0
    def __del__(self):
        """remove window number in nr_set"""
        Counter.nr_set.remove(self._nr)

    def __bool__(self):
        return self.free
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, t):
        self._start_time = t

    @property
    def is_measure_time(self):
        return self._is_measure_time

    @is_measure_time.setter
    def is_measure_time(self, ft):
        self._is_measure_time = ft

    @property
    def free(self):
        return self._free

    @free.setter
    def free(self, ft):
        self._free = ft

    @property
    def client_in(self):
        return self._client_in

    @client_in.setter
    def client_in(self, client_in):
        self._client_in = client_in

    @property
    def nr(self):
        return self._nr

    @property
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

    def __str__(self) -> str:
        return "Window nr: " + str(self.nr) + "\n\t a: " + str(self.a) + " b: " + str(self.b) + "\n\t free: " + str(self.free)

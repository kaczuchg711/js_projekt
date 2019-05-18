
class myQueue():
    def __init__(self):
        self.tab = []
        self.num = 0

    def pop(self):
        self.tab[0].wyjscie()
        self.tab.pop(0)
        return

    def push(self, x):
        x.wejscie()
        self.tab.append(x)

    def __str__(self):
        return [x.__str__() for x in self.tab].__str__()

    def __iter__(self):
        return self

    def __next__(self):
        if(self.tab.__len__() == 0):
            raise StopIteration
        return self.pop()


class MyQueue():
    def __init__(self, tab=[]):
        self.tab = tab

    def pop(self):
        self.tab[0].wyjscie()
        self.tab.pop(0)
        return

    def push(self, x):
        x.wejscie()
        self.tab.append(x)

    def __str__(self):
        return [x.__str__() for x in self.tab].__str__()

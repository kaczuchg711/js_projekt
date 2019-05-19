
class myQueue():
    def __init__(self,napis):
        self.tab = []
        self.num = 0
        self.napis = napis

    def pop(self):
        if (self.tab.__len__() == 0):
            print("wtf")
        return self.tab.pop(0)


    def push(self, x):
        x.wejscie()
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
        if(self.tab.__len__() == 0):
            raise StopIteration
        return self.pop()

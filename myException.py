class NoProperCounter(Exception):
    def __init__(self):
        print("brak odpowiedniej bramki")

class NoFreeCounter(Exception):
    def __init__(self):
        print("brak wolnej bramki)")
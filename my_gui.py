from tkinter import *


class GUI:
    def __init__(self):
        self._root = Tk()
        self._frame1 = Frame(self._root)  # kontener na górne przyciski
        self._frame2 = Frame(self._root)  # kolejka zwykla
        self._frame3 = Frame(self._root)  # kolejka VIP
        self._frame4 = Frame(self._root)  # okienka
        self._frame5 = Frame(self._root)  # A
        self._frame6 = Frame(self._root)  # B
        self._framelast = Frame(self._root)  # koniec

        self._buttons = [*[Button(self._frame1) for i in range(5)],  # gorne
                         Button(self._framelast)]  # koniec

        self._checkbuttons = [*[Checkbutton(self._frame5) for i in range(3)],  # A
                              *[Checkbutton(self._frame6) for i in range(3)]]  # B

        self._labels = [Label(self._frame2), Label(self._frame3),  # kolejki
                        *[Label(self._frame4) for i in range(3)],  # okienka
                        Label(self._frame5),  # A
                        Label(self._frame6)]  # B

        self._texts = [Text(self._frame2), Text(self._frame3)]
        self.buttons_config()
        self.label_conf()
        self.text_conf()
        self.checkbuttons_config()

    def checkbuttons_config(self):
        self._checkbuttons[0].config(width=14,text="1")
        self._checkbuttons[1].config(width=14,text="2")
        self._checkbuttons[2].config(width=14,text="3")
        self._checkbuttons[3].config(width=14,text="4")
        self._checkbuttons[4].config(width=14,text="5")
        self._checkbuttons[5].config(width=14,text="6")

    def buttons_config(self):
        self._buttons[0].config(text="A", width=6, )
        self._buttons[1].config(text="A VIP", width=6)
        self._buttons[2].config(text="B", width=6)
        self._buttons[3].config(text="B VIP", width=6)
        self._buttons[4].config(text="Następny", width=6)
        self._buttons[5].config(text="Koniec", width=6, command=lambda: exit(0))

    def label_conf(self):
        self._labels[0].config(text="kolejka zwykla", width=15)
        self._labels[1].config(text="kolejka VIP", width=15)
        self._labels[2].config(text="Okienko 1", width=15)
        self._labels[3].config(text="Okienko 2", width=15)
        self._labels[4].config(text="Okienko 3", width=15)
        self._labels[5].config(text="A")
        self._labels[6].config(text="B")

    def text_conf(self):
        self._texts[0].config(height=1)
        self._texts[1].config(height=1)

    def pack(self):
        self._frame1.pack()
        self._frame2.pack()
        self._frame3.pack()
        self._frame4.pack()
        self._frame5.pack()
        self._frame6.pack()
        self._framelast.pack()
        for x in self._buttons: x.pack(side=LEFT)
        for x in self._labels: x.pack(side=LEFT)
        for x in self._texts: x.pack(side=LEFT)
        for x in self._checkbuttons: x.pack(side=LEFT)

    def go(self):
        mainloop()

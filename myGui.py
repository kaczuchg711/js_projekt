from typing import Iterable

import pygame


class myGui:
    def __init__(self):
        pygame.init()
        self.__screen_lenght = 800
        self.__screen_width = 800
        self.__screen = pygame.display.set_mode((self.__screen_lenght, self.__screen_width))
        self.__exit = False
        self.__mouse_pos = []
        self.__b = [Button() for x in range(6)]
        self.__cb = [CheckBox() for x in range(6)]
        self.__t = [0 for x in range(6)]
        self.__how_many_in_queue = [0 for x in range(4)]
        self.button_mod()
        self.CheckBox()

    def button_mod(self):

        height = 2 / 15. * self.screen_width

        self.b[0].change_pos(1 / 8 * self.screen_lenght + self.b[0].length / 2., height)
        self.b[0].color = (255, 0, 0)

        self.b[1].change_pos(2 / 8 * self.screen_lenght + self.b[1].length / 2., height)
        self.b[1].color = (0, 0, 255)
        self.b[1].change_writing("B")

        self.b[2].change_pos(3 / 8 * self.screen_lenght + self.b[2].length / 2., height)
        self.b[2].color = (150, 25, 0)
        self.b[2].change_writing("A VIP")

        self.b[3].change_pos(4 / 8 * self.screen_lenght + self.b[3].length / 2., height)
        self.b[3].color = (0, 25, 150)
        self.b[3].change_writing("B VIP")

        self.b[4].change_pos(6 / 8 * self.screen_lenght + self.b[4].length / 2., height)
        self.b[4].color = (200, 200, 200)
        self.b[4].change_writing("Next")
        self.b[4].change_writing_color((0, 0, 0))

        self.b[5].change_pos(self.screen_lenght / 2 - self.b[5].length / 2., self.screen_width - (self.b[5].width + 10))
        self.b[5].color = (255, 0, 128)
        self.b[5].change_writing("Koniec")
        self.b[5].change_writing_color((0, 0, 0))

    def CheckBox(self):
        self.cb[0].change_pos(3.35 / 8 * self.screen_lenght, 5.3 / 10 * self.screen_lenght)
        self.cb[1].change_pos(4.35 / 8 * self.screen_lenght, 5.3 / 10 * self.screen_lenght)
        self.cb[2].change_pos(5.35 / 8 * self.screen_lenght, 5.3 / 10 * self.screen_lenght)
        self.cb[3].change_pos(3.35 / 8 * self.screen_lenght, 6.3 / 10 * self.screen_lenght)
        self.cb[4].change_pos(4.35 / 8 * self.screen_lenght, 6.3 / 10 * self.screen_lenght)
        self.cb[5].change_pos(5.35 / 8 * self.screen_lenght, 6.3 / 10 * self.screen_lenght)

    def get_cb_to_check(self):
        return [x for x in self.cb if x.on_mouse]

    def mouse_on_obj(self, obj):
        if obj.x < self.mouse_pos[0] < obj.x + obj.length \
                and obj.y < self.mouse_pos[1] < obj.y + obj.width:
            obj.on_mouse = True
            return True
        else:
            obj.on_mouse = False
            return False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                """kończenie programu"""
                self.exit = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.exit = True
            if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_on_obj(self.b[5]):
                self.exit = True

            if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_on_obj(self.b[0]):
                """zmiana koloru pierwszego przycisku"""
                if self.b[0].color != (255, 0, 0):
                    self.b[0].color = (255, 0, 0)
                else:
                    self.b[0].color = (0, 0, 255)

            for x in self.cb:
                if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_on_obj(x):
                    if x.is_check:
                        x.is_check = False
                        print(x.is_check)
                    else:
                        x.is_check = True
                        print(x.is_check)
            else:
                pass

    def drawing(self):

        font = pygame.font.SysFont("dejavumathtexgyre", 18)  # txt

        for x in self.b:
            """przyciski normalne"""
            pygame.draw.rect(self.screen, x.color, x.shape)
            text_rect = x.label.get_rect(center=(x.length / 2 + x.x, x.width / 2 + x.y))  # centrowanie npaisu
            # ile czeka
            self.screen.blit(x.label, text_rect)

        for i,x in enumerate(self.b[:2]):
            label = font.render(self.__how_many_in_queue[i].__str__(), 1, (255, 255, 255))
            text_rect = x.label.get_rect(center=(x.length / 2 + x.x, 1.2 * x.width + x.y))
            self.screen.blit(label, text_rect)

        for i,x in enumerate(self.b[2:4]):
            label = font.render(self.__how_many_in_queue[i].__str__(), 1, (255, 255, 255))
            text_rect = x.label.get_rect(center=(x.length / 2 + x.x + 10, 1.2 * x.width + x.y))
            self.screen.blit(label, text_rect)

        for x in self.cb:
            """check box"""
            img_rect = x.img.get_rect(center=(x.x, x.y))
            self.screen.blit(x.img, (x.x, x.y))

        # lines
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 4 / 10 * self.screen_lenght),
                         (7 / 8 * self.screen_lenght, 4 / 10 * self.screen_lenght), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 5 / 10 * self.screen_lenght),
                         (7 / 8 * self.screen_lenght, 5 / 10 * self.screen_lenght), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 6 / 10 * self.screen_lenght),
                         (7 / 8 * self.screen_lenght, 6 / 10 * self.screen_lenght), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 7 / 10 * self.screen_lenght),
                         (7 / 8 * self.screen_lenght, 7 / 10 * self.screen_lenght), 1)
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 8 / 10 * self.screen_lenght),
                         (7 / 8 * self.screen_lenght, 8 / 10 * self.screen_lenght), 1)
        # vertical
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 4 / 10 * self.screen_lenght),
                         (1 / 8 * self.screen_lenght, 8 / 10 * self.screen_lenght), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (3 / 8 * self.screen_lenght, 4 / 10 * self.screen_lenght),
                         (3 / 8 * self.screen_lenght, 8 / 10 * self.screen_lenght), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (4 / 8 * self.screen_lenght, 4 / 10 * self.screen_lenght),
                         (4 / 8 * self.screen_lenght, 8 / 10 * self.screen_lenght), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (5 / 8 * self.screen_lenght, 4 / 10 * self.screen_lenght),
                         (5 / 8 * self.screen_lenght, 8 / 10 * self.screen_lenght), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (6 / 8 * self.screen_lenght, 4 / 10 * self.screen_lenght),
                         (6 / 8 * self.screen_lenght, 8 / 10 * self.screen_lenght), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (7 / 8 * self.screen_lenght, 4 / 10 * self.screen_lenght),
                         (7 / 8 * self.screen_lenght, 8 / 10 * self.screen_lenght), 1)

        # napisy

        label = font.render("Okienko 1", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(3.5 / 8 * self.screen_lenght, 3.6 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        label = font.render("Okienko 2", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(4.5 / 8 * self.screen_lenght, 3.6 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        label = font.render("Okienko 3", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(5.5 / 8 * self.screen_lenght, 3.6 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        label = font.render("Łącznie", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 3.6 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        label = font.render("Sprawa A", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 4.4 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        label = font.render("Sprawa B", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 5.2 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        label = font.render("Łącznie", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 6 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        # łącznie
        label = font.render(self.t[0].__str__(), 1, (255, 255, 255))
        text_rect = label.get_rect(center=(3.5 / 8 * self.screen_lenght, 6 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        label = font.render(self.t[1].__str__(), 1, (255, 255, 255))
        text_rect = label.get_rect(center=(4.5 / 8 * self.screen_lenght, 6 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        label = font.render(self.t[2].__str__(), 1, (255, 255, 255))
        text_rect = label.get_rect(center=(5.5 / 8 * self.screen_lenght, 6 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        label = font.render(self.t[3].__str__(), 1, (255, 255, 255))
        text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 6 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        label = font.render(self.t[4].__str__(), 1, (255, 255, 255))
        text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 5.2 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

        label = font.render(self.t[5].__str__(), 1, (255, 255, 255))
        text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 4.4 / 8 * self.screen_lenght))
        self.screen.blit(label, text_rect)

    def go(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.drawing()
        pygame.display.flip()

    @property
    def screen_lenght(self):
        return self.__screen_lenght

    @property
    def t(self):
        return self.__t

    @t.setter
    def t(self, v):
        self.__t = v

    @property
    def how_many_in_queue(self):
        return self.__t

    @how_many_in_queue.setter
    def how_many_in_queue(self, v):
        self.__how_many_in_queue = v

    @property
    def screen_width(self):
        return self.__screen_width

    @property
    def screen(self):
        return self.__screen

    @property
    def exit(self):
        return self.__exit

    @exit.setter
    def exit(self, tf):
        self.__exit = tf

    @property
    def mouse_pos(self):
        return self.__mouse_pos

    @mouse_pos.setter
    def mouse_pos(self, mp):
        self.__mouse_pos = mp

    @property
    def b(self):
        return self.__b

    @property
    def cb(self):
        return self.__cb


class Button:
    def __init__(self, x=30, y=30, length=80, width=50, color=(0, 128, 255), writing="A",
                 writing_color=(255, 255, 255)):
        self.__x = x
        self.__y = y
        self.__lenght = length
        self.__width = width
        self.__shape = pygame.Rect(x, y, length, width)
        self.__color = color
        self.__writing_color = writing_color
        self.__font = pygame.font.SysFont("monospace", 12)  # txt
        self.__writing = writing
        self.__label = self.__font.render(writing, 1, (writing_color))
        self.__on_mouse = False

    def change_pos(self, x, y):
        self.__x = x
        self.__y = y
        self.__shape = pygame.Rect(x, y, self.__lenght, self.__width)

    def change_writing(self, writing):
        self.__writing = writing
        self.__label = self.__font.render(writing, 1, (self.__writing_color))

    def change_writing_color(self, writing_color):
        self.__writing_color = writing_color
        self.__label = self.__font.render(self.__writing, 1, (writing_color))

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def on_mouse(self):
        return self.__color

    @on_mouse.setter
    def on_mouse(self, ft):
        self.__on_mouse = ft

    @property
    def length(self):
        return self.__lenght

    @property
    def width(self):
        return self.__width

    @property
    def shape(self):
        return self.__shape

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, l):
        self.__lenght = l


class CheckBox(Button):
    def __init__(self):
        super().__init__()
        self.__img = pygame.image.load("nocheck.bmp")
        self.__is_check = False

    @property
    def img(self):
        return self.__img

    @img.setter
    def img(self, img):
        self.__img = img

    @property
    def is_check(self):
        return self.__is_check

    @is_check.setter
    def is_check(self, ft):
        if ft:
            self.img = pygame.image.load("ischeck.bmp")
        else:
            self.img = pygame.image.load("nocheck.bmp")
        self.__is_check = ft
from typing import Iterable
import pygame
from klienci.KlientZwykly import *
from klienci.KlientVIP import *
from Counter import *
from myQueue import *
from myException import *
import time
from TimeMeasurement import *
import os


class myGui:
    restart = False

    def __init__(self):
        pygame.init()
        self.__screen_lenght = 1000
        self.__screen_width = 900
        self.__screen = pygame.display.set_mode((self.__screen_lenght, self.__screen_width))
        self.__exit = False
        self.__mouse_pos = []
        self.__b = [Button() for x in range(6)]
        self._restart_button = Button()
        self.__cb = [CheckBox() for x in range(6)]
        self.__t = [0 for x in range(6)]
        self.__number_of_clients = [0 for x in range(4)]
        self.button_mod()
        self.CheckBox_mod()
        self.__nq = myQueue("normalna")
        self.__vq = myQueue("vip")
        self.__counters = [Counter(0), Counter(1), Counter(2)]

        self.__info_under_next = ""
        self.__data = TimeMeasurement()
        self.container_for_time = time.time()
        self._time_for_tick = 1

        self.font = pygame.font.SysFont("dejavumathtexgyre", 18)  # txt
        self.skandal = self.font.render("", 1, (255, 0, 0))



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
        self.b[5].color = (255, 255, 128)
        self.b[5].change_writing("Koniec")
        self.b[5].change_writing_color((0, 0, 0))

        self._restart_button.change_pos(self.screen_lenght / 2 - self._restart_button.length / 2.,
                                        self.screen_width - (self._restart_button.width + 10))
        self._restart_button.change_writing("Jeszcze raz")

    def CheckBox_mod(self):
        self.cb[0].change_pos(3.35 / 8 * self.screen_lenght, 5.3 / 10 * self.screen_width)
        self.cb[1].change_pos(4.35 / 8 * self.screen_lenght, 5.3 / 10 * self.screen_width)
        self.cb[2].change_pos(5.35 / 8 * self.screen_lenght, 5.3 / 10 * self.screen_width)
        self.cb[3].change_pos(3.35 / 8 * self.screen_lenght, 6.3 / 10 * self.screen_width)
        self.cb[4].change_pos(4.35 / 8 * self.screen_lenght, 6.3 / 10 * self.screen_width)
        self.cb[5].change_pos(5.35 / 8 * self.screen_lenght, 6.3 / 10 * self.screen_width)

    def mouse_on_obj(self, obj):
        if obj.x < self.mouse_pos[0] < obj.x + obj.length \
                and obj.y < self.mouse_pos[1] < obj.y + obj.width:
            obj.on_mouse = True
            return True
        else:
            obj.on_mouse = False
            return False

    def wait(self):
        """ogladanie statystyk"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    os.sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_on_obj(self._restart_button):
                    myGui.restart = True
                    return

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                """kończenie programu"""
                self.exit = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.exit = True
            if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_on_obj(self.b[5]):
                self.screen.fill((0, 0, 0))  # odświerzanie
                self.end_drawing()
                pygame.display.flip()
                self.wait()
                self.exit = True

            if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_on_obj(self.b[0]):
                """dodawanie klientów"""
                self.nq.push(KlientZwykly("A"))
                self.number_of_clients[0] += 1
                print("dodanie klienta A")
                print("kolejka VIP", self.vq)
                print("kolejka zwykla", self.nq)
            if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_on_obj(self.b[1]):
                self.nq.push(KlientZwykly("B"))
                self.number_of_clients[1] += 1
                print("dodawanie klientów B")
                print("kolejka VIP", self.vq)
                print("kolejka zwykla", self.nq)
            if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_on_obj(self.b[2]):
                self.vq.push(KlientVIP("A"))
                self.number_of_clients[2] += 1
                print("dodawanie klientów VIP A")
                print("kolejka VIP", self.vq)
                print("kolejka zwykla", self.nq)
            if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_on_obj(self.b[3]):
                self.vq.push(KlientVIP("B"))
                self.number_of_clients[3] += 1
                print("dodawanie klientów VIP B")
                print("kolejka VIP", self.vq)
                print("kolejka zwykla", self.nq)

            if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_on_obj(self.b[4]):
                """przyciskanie next"""
                try:
                    if any(self.counters):
                        if not self.vq.empty():
                            temp_klient = self.vq.get_first()
                            if temp_klient.kind == "A":
                                for x in self.counters:
                                    print(x)
                                    if x.free and x.a:
                                        x.free = False
                                        x.client_in = self.vq.pop()

                                        self.__data(x.client_in.wyjscie(), "A", "VIP", x.nr)
                                        self.number_of_clients[2] -= 1
                                        break
                                else:
                                    raise NoProperCounter
                            elif temp_klient.kind == "B":
                                for x in self.counters:
                                    print(x)
                                    if x.free and x.b:
                                        x.free = False
                                        x.client_in = self.vq.pop()
                                        self.__data(x.client_in.wyjscie(), "B", "VIP", x.nr)
                                        self.number_of_clients[3] -= 1
                                        break
                                else:
                                    raise NoProperCounter
                        elif not self.nq.empty():
                            temp = self.nq.get_first()
                            if temp.kind == "A":
                                for x in self.counters:
                                    print(x)
                                    if x.free and x.a:
                                        x.free = False
                                        x.client_in = self.nq.pop()
                                        self.__data(x.client_in.wyjscie(), "A", "N", x.nr)
                                        self.number_of_clients[0] -= 1
                                        break
                                else:
                                    raise NoProperCounter
                            elif temp.kind == "B":
                                for x in self.counters:
                                    print(x)
                                    if x.free and x.b:
                                        x.free = False
                                        x.client_in = self.nq.pop()
                                        self.__data(x.client_in.wyjscie(), "B", "N", x.nr)
                                        self.number_of_clients[1] -= 1
                                        break
                                else:
                                    raise NoProperCounter
                    else:
                        raise NoFreeCounter
                except NoProperCounter:
                    self.info_under_next = "brak odpowiedniej bramki"
                except NoFreeCounter:
                    self.info_under_next = "brak wolnej bramki"
                else:
                    self.info_under_next = ""

            for x in self.cb:
                if event.type == pygame.MOUSEBUTTONDOWN and self.mouse_on_obj(x):
                    if x.is_check:
                        x.is_check = False
                        print(x.is_check)
                    else:
                        x.is_check = True
                        print(x.is_check)

        for i, x in enumerate(self.cb):

            if x in self.cb[:3]:
                if self.cb[i].is_check and not self.counters[i].a:
                    self.counters[i].a = True
                    print(self.counters[i])
                if not self.cb[i].is_check and self.counters[i].a:
                    self.counters[i].a = False
                    print(self.counters[i])

            if x in self.cb[3:]:
                if self.cb[i].is_check and not self.counters[i % 3].b:
                    self.counters[i % 3].b = True
                    print(self.counters[i % 3])
                if not self.cb[i].is_check and self.counters[i % 3].b:
                    self.counters[i % 3].b = False
                    print(self.counters[i % 3])

        for x in self.counters:
            """zmiana na True po uplywie 3 s "czas obslugiwania klienta" """
            if not x.free and not x.is_measure_time:
                x.start_time = time.time()
                x.is_measure_time = True
            if x.is_measure_time and (time.time() - x.start_time) > 3:
                x.free = True
                x.is_measure_time = False
                x.client_in = 0
                print("koniec obslugi")

    def end_drawing(self):

        font = pygame.font.SysFont("dejavumathtexgyre", 18)  # txt

        # lines
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 1 / 10 * self.screen_width),
                         (7 / 8 * self.screen_lenght, 1 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 2 / 10 * self.screen_width),
                         (7 / 8 * self.screen_lenght, 2 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 3 / 10 * self.screen_width),
                         (7 / 8 * self.screen_lenght, 3 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 4 / 10 * self.screen_width),
                         (7 / 8 * self.screen_lenght, 4 / 10 * self.screen_width), 1)
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 5 / 10 * self.screen_width),
                         (7 / 8 * self.screen_lenght, 5 / 10 * self.screen_width), 1)
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 6 / 10 * self.screen_width),
                         (7 / 8 * self.screen_lenght, 6 / 10 * self.screen_width), 1)
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 7 / 10 * self.screen_width),
                         (7 / 8 * self.screen_lenght, 7 / 10 * self.screen_width), 1)
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 8 / 10 * self.screen_width),
                         (7 / 8 * self.screen_lenght, 8 / 10 * self.screen_width), 1)
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 9 / 10 * self.screen_width),
                         (7 / 8 * self.screen_lenght, 9 / 10 * self.screen_width), 1)

        # vertical
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 1 / 10 * self.screen_width),
                         (1 / 8 * self.screen_lenght, 9 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (3 / 8 * self.screen_lenght, 1 / 10 * self.screen_width),
                         (3 / 8 * self.screen_lenght, 9 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (4 / 8 * self.screen_lenght, 1 / 10 * self.screen_width),
                         (4 / 8 * self.screen_lenght, 9 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (5 / 8 * self.screen_lenght, 1 / 10 * self.screen_width),
                         (5 / 8 * self.screen_lenght, 9 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (6 / 8 * self.screen_lenght, 1 / 10 * self.screen_width),
                         (6 / 8 * self.screen_lenght, 9 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (7 / 8 * self.screen_lenght, 1 / 10 * self.screen_width),
                         (7 / 8 * self.screen_lenght, 9 / 10 * self.screen_width), 1)

        # napisy
        s = ["Klient Zwykły","Okienko 1","Okienko 2","Okienko 3" , "Łącznie"]
        l = [2] + [x + 3.5 for x in range(4)]

        for string,lenght in zip(s,l):
            label = font.render(string, 1, (255, 255, 255))
            text_rect = label.get_rect(center=(lenght / 8 * self.screen_lenght, 1.2 / 8 * self.screen_width))
            self.screen.blit(label, text_rect)

        label = font.render("Sprawa A", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 2 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        prepare_time = lambda a: (str(round(a, 2)))

        for i, x in enumerate([x + 3.5 for x in range(3)]):
            """klient zwykly wiersz A"""
            label = font.render(prepare_time(self.__data.time_N_A_issue_for_counter[i]), 1, (255, 255, 255))
            text_rect = label.get_rect(center=(x / 8 * self.screen_lenght, 2 / 8 * self.screen_width))
            self.screen.blit(label, text_rect)

        label = font.render(prepare_time(sum(self.__data.time_N_A_issue_for_counter)), 1, (255, 255, 255))
        text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 2 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        for i, x in enumerate([x + 3.5 for x in range(3)]):
            """wiersz B"""
            label = font.render(prepare_time(self.__data.time_N_B_issue_for_counter[i]), 1, (255, 255, 255))
            text_rect = label.get_rect(center=(x / 8 * self.screen_lenght, 2.8 / 8 * self.screen_width))
            self.screen.blit(label, text_rect)

        label = font.render(prepare_time(sum(self.__data.time_N_B_issue_for_counter)), 1, (255, 255, 255))
        text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 2.8 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        for i, x in enumerate([x + 3.5 for x in range(3)]):
            """wiersz łącznie"""
            label = font.render(
                prepare_time(self.__data.time_N_A_issue_for_counter[i] + self.__data.time_N_B_issue_for_counter[i]), 1,
                (255, 255, 255))
            text_rect = label.get_rect(center=(x / 8 * self.screen_lenght, 3.6 / 8 * self.screen_width))
            self.screen.blit(label, text_rect)

        label = font.render(
            prepare_time(sum(self.__data.time_N_A_issue_for_counter + self.__data.time_N_B_issue_for_counter)), 1,
            (255, 255, 255))
        text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 3.6 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        for i, x in enumerate([x + 3.5 for x in range(3)]):
            """klient VIP wiersz A"""
            label = font.render(prepare_time(self.__data.time_V_A_issue_for_counter[i]), 1, (255, 255, 255))
            text_rect = label.get_rect(center=(x / 8 * self.screen_lenght, 5.2 / 8 * self.screen_width))
            self.screen.blit(label, text_rect)

        label = font.render(prepare_time(sum(self.__data.time_V_A_issue_for_counter)), 1, (255, 255, 255))
        text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 5.2 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        for i, x in enumerate([x + 3.5 for x in range(3)]):
            """wiersz B"""
            label = font.render(prepare_time(self.__data.time_V_B_issue_for_counter[i]), 1, (255, 255, 255))
            text_rect = label.get_rect(center=(x / 8 * self.screen_lenght, 6 / 8 * self.screen_width))
            self.screen.blit(label, text_rect)

        label = font.render(prepare_time(sum(self.__data.time_V_B_issue_for_counter)), 1, (255, 255, 255))
        text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 6 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        for i, x in enumerate([x + 3.5 for x in range(3)]):
            """wiersz łącznie"""
            label = font.render(
                prepare_time(self.__data.time_V_A_issue_for_counter[i] + self.__data.time_V_B_issue_for_counter[i]), 1,
                (255, 255, 255))
            text_rect = label.get_rect(center=(x / 8 * self.screen_lenght, 6.8 / 8 * self.screen_width))
            self.screen.blit(label, text_rect)

        label = font.render(
            prepare_time(sum(self.__data.time_V_A_issue_for_counter + self.__data.time_V_B_issue_for_counter)), 1,
            (255, 255, 255))
        text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 6.8 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        label = font.render("Sprawa B", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 2.8 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        # łącznie

        label = font.render("Łącznie", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 3.6 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        label = font.render("Klient VIP", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 4.4 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        label = font.render("Sprawa A", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 5.2 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        label = font.render("Sprawa B", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 6 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        label = font.render("Łącznie", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 6.8 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        # reset
        pygame.draw.rect(self.screen, self._restart_button.color, self._restart_button.shape)
        text_rect = self._restart_button.label.get_rect(center=(self._restart_button.length / 2 + self._restart_button.x, self._restart_button.width / 2 + self._restart_button.y))  # centrowanie npaisu
        self.screen.blit(self._restart_button.label, text_rect)
    def drawing(self):

        font = pygame.font.SysFont("dejavumathtexgyre", 18)  # txt

        for x in self.b:
            """przyciski normalne"""
            pygame.draw.rect(self.screen, x.color, x.shape)
            text_rect = x.label.get_rect(center=(x.length / 2 + x.x, x.width / 2 + x.y))  # centrowanie npaisu
            # ile czeka
            self.screen.blit(x.label, text_rect)

        for i, x in enumerate(self.b[:2]):
            label = font.render(self.number_of_clients[i].__str__(), 1, (255, 255, 255))
            text_rect = x.label.get_rect(center=(x.length / 2 + x.x, 1.2 * x.width + x.y))
            self.screen.blit(label, text_rect)

        # to stworzone tylko dla przesuniecia tego + 10
        for i, x in enumerate(self.b[2:4]):
            label = font.render(self.number_of_clients[i + 2].__str__(), 1, (255, 255, 255))
            text_rect = x.label.get_rect(center=(x.length / 2 + x.x + 10, 1.2 * x.width + x.y))
            self.screen.blit(label, text_rect)

        text_rect = self.b[2].label.get_rect(center=(self.b[2].length / 2 + self.b[2].x + 10, 1.5 * self.b[2].width + self.b[2].y))
        self.screen.blit(self.skandal,text_rect)

        label = font.render(self.info_under_next, 1, (255, 255, 255))
        """dla next"""
        text_rect = self.b[4].label.get_rect(
            center=(self.b[4].length / 2 + 0.87 * self.b[4].x, 1.2 * self.b[4].width + self.b[4].y))
        self.screen.blit(label, text_rect)

        for x in self.cb:
            """check box"""
            img_rect = x.img.get_rect(center=(x.x, x.y))
            self.screen.blit(x.img, (x.x, x.y))

        # lines
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 4 / 10 * self.screen_width),
                         (6 / 8 * self.screen_lenght, 4 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 5 / 10 * self.screen_width),
                         (6 / 8 * self.screen_lenght, 5 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 6 / 10 * self.screen_width),
                         (6 / 8 * self.screen_lenght, 6 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 7 / 10 * self.screen_width),
                         (6 / 8 * self.screen_lenght, 7 / 10 * self.screen_width), 1)
        # pygame.draw.line(self.screen, (255, 255, 255),
        #                  (1 / 8 * self.screen_lenght, 8 / 10 * self.screen_width),
        #                  (7 / 8 * self.screen_lenght, 8 / 10 * self.screen_width), 1)
        # vertical
        pygame.draw.line(self.screen, (255, 255, 255),
                         (1 / 8 * self.screen_lenght, 4 / 10 * self.screen_width),
                         (1 / 8 * self.screen_lenght, 7 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (3 / 8 * self.screen_lenght, 4 / 10 * self.screen_width),
                         (3 / 8 * self.screen_lenght, 7 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (4 / 8 * self.screen_lenght, 4 / 10 * self.screen_width),
                         (4 / 8 * self.screen_lenght, 7 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (5 / 8 * self.screen_lenght, 4 / 10 * self.screen_width),
                         (5 / 8 * self.screen_lenght, 7 / 10 * self.screen_width), 1)

        pygame.draw.line(self.screen, (255, 255, 255),
                         (6 / 8 * self.screen_lenght, 4 / 10 * self.screen_width),
                         (6 / 8 * self.screen_lenght, 7 / 10 * self.screen_width), 1)

        # pygame.draw.line(self.screen, (255, 255, 255),
        #                  (7 / 8 * self.screen_lenght, 4 / 10 * self.screen_width),
        #                  (7 / 8 * self.screen_lenght, 8 / 10 * self.screen_width), 1)

        # napisy

        temp_str = ""

        if not self.counters[0].free:
            temp_str = " o"

        label = font.render("Okienko 1" + temp_str, 1, (255, 255, 255))
        text_rect = label.get_rect(center=(3.5 / 8 * self.screen_lenght, 3.6 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)
        temp_str = ""

        if not self.counters[1].free:
            temp_str = " o"

        label = font.render("Okienko 2" + temp_str, 1, (255, 255, 255))
        text_rect = label.get_rect(center=(4.5 / 8 * self.screen_lenght, 3.6 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)
        temp_str = ""

        if not self.counters[2].free:
            temp_str = " o"

        label = font.render("Okienko 3" + temp_str, 1, (255, 255, 255))
        text_rect = label.get_rect(center=(5.5 / 8 * self.screen_lenght, 3.6 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)
        temp_str = ""

        # label = font.render("Łącznie", 1, (255, 255, 255))
        # text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 3.6 / 8 * self.screen_width))
        # self.screen.blit(label, text_rect)

        label = font.render("Sprawa A", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 4.4 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        label = font.render("Sprawa B", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 5.2 / 8 * self.screen_width))
        self.screen.blit(label, text_rect)

        # łącznie

        # label = font.render("Łącznie", 1, (255, 255, 255))
        # text_rect = label.get_rect(center=(2 / 8 * self.screen_lenght, 6 / 8 * self.screen_width))
        # self.screen.blit(label, text_rect)
        #
        # label = font.render(self.t[0].__str__(), 1, (255, 255, 255))
        # text_rect = label.get_rect(center=(3.5 / 8 * self.screen_lenght, 6 / 8 * self.screen_width))
        # self.screen.blit(label, text_rect)
        #
        # label = font.render(self.t[1].__str__(), 1, (255, 255, 255))
        # text_rect = label.get_rect(center=(4.5 / 8 * self.screen_lenght, 6 / 8 * self.screen_width))
        # self.screen.blit(label, text_rect)
        #
        # label = font.render(self.t[2].__str__(), 1, (255, 255, 255))
        # text_rect = label.get_rect(center=(5.5 / 8 * self.screen_lenght, 6 / 8 * self.screen_width))
        # self.screen.blit(label, text_rect)
        #
        # label = font.render(self.t[3].__str__(), 1, (255, 255, 255))
        # text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 6 / 8 * self.screen_width))
        # self.screen.blit(label, text_rect)
        #
        # label = font.render(self.t[4].__str__(), 1, (255, 255, 255))
        # text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 5.2 / 8 * self.screen_width))
        # self.screen.blit(label, text_rect)
        #
        # label = font.render(self.t[5].__str__(), 1, (255, 255, 255))
        # text_rect = label.get_rect(center=(6.5 / 8 * self.screen_lenght, 4.4 / 8 * self.screen_width))
        # self.screen.blit(label, text_rect)

        #

    def go(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.screen.fill((0, 0, 0))  # odświerzanie
        self.drawing()
        self.events()

        if ((time.time() - self.container_for_time) % 2 > 1):
            for x in self.vq:

                self.skandal = self.font.render(x.tick(), 1, (255, 0, 0))

            for x in self.nq:
                x.tick()
            self.container_for_time = time.time()

        pygame.display.flip()

    # gs

    @property
    def info_under_next(self):
        return self.__info_under_next

    @info_under_next.setter
    def info_under_next(self, text):
        self.__info_under_next = text

    @property
    def time_for_tick(self):
        return self._time_for_tick

    @time_for_tick.setter
    def time_for_tick(self, t):
        self._time_for_tick = t

    @property
    def counters(self):
        return self.__counters

    @counters.setter
    def counters(self, counters):
        self.__counters = counters

    @property
    def nq(self):
        return self.__nq

    @nq.setter
    def nq(self, nq):
        self.__nq = nq

    @property
    def vq(self):
        return self.__vq

    @vq.setter
    def vq(self, vq):
        self.__vq = vq

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
    def number_of_clients(self):
        return self.__number_of_clients

    @number_of_clients.setter
    def number_of_clients(self, v):
        self.__number_of_clients = v

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

    #


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

    # gs

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

    #


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

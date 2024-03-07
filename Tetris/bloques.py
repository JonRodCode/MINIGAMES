import pygame
from abc import ABC, abstractmethod
class Bloque(ABC):
    @abstractmethod
    def __init__(self,screen,pos):
        self.figura = pygame.Surface((20,20))
        self.bloque = []
        self.screen = screen
        self.posicion = "1"
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.crear_figura()
    @abstractmethod
    def crear_figura(self):
        pass
    def draw(self):
        for rect in self.bloque:
            self.screen.blit(self.figura,rect)
class Bloque_1(Bloque):
    def __init__(self,screen,pos):
        super().__init__(screen,pos)
        self.figura.fill("darkgreen")

    def crear_figura(self):
        if bool(self.bloque) == False:
            for i in range(3):
                figura_rect = self.figura.get_rect(topleft = (self.pos_x, self.pos_y))
                self.bloque.append(figura_rect)
                self.pos_x += 20
            figura_rect = self.figura.get_rect(topleft=(self.pos_x-20*2, self.pos_y +20))
            self.bloque.append(figura_rect)
class Bloque_2(Bloque):
    def __init__(self,screen,pos):
        super().__init__(screen,pos)
        self.figura.fill("yellow")

    def crear_figura(self):
        if bool(self.bloque) == False:
            for i in range(3):
                figura_rect = self.figura.get_rect(topleft=(self.pos_x, self.pos_y))
                self.bloque.append(figura_rect)
                self.pos_x += 20
            figura_rect = self.figura.get_rect(topleft=(self.pos_x - 20, self.pos_y + 20))
            self.bloque.append(figura_rect)
class Bloque_3(Bloque):
    def __init__(self,screen,pos):
        super().__init__(screen,pos)
        self.figura.fill("darkviolet")

    def crear_figura(self):
        if bool(self.bloque) == False:
            for i in range(3):
                figura_rect = self.figura.get_rect(topleft=(self.pos_x, self.pos_y))
                self.bloque.append(figura_rect)
                self.pos_x += 20
            figura_rect = self.figura.get_rect(topleft=(self.pos_x - 20*3, self.pos_y + 20))
            self.bloque.append(figura_rect)
class Bloque_4(Bloque):
    def __init__(self,screen,pos):
        super().__init__(screen,pos)
        self.figura.fill("darkblue")

    def crear_figura(self):
        if bool(self.bloque) == False:
            for i in range(2):
                figura_rect = self.figura.get_rect(topleft=(self.pos_x, self.pos_y))
                self.bloque.append(figura_rect)
                self.pos_x += 20
            self.pos_x -= 40
            self.pos_y += 20
            for i in range(2):
                figura_rect = self.figura.get_rect(topleft=(self.pos_x, self.pos_y))
                self.bloque.append(figura_rect)
                self.pos_x += 20
class Bloque_5(Bloque):
    def __init__(self,screen,pos):
        super().__init__(screen,pos)
        self.figura.fill("red")

    def crear_figura(self):
        if bool(self.bloque) == False:
            for i in range(4):
                figura_rect = self.figura.get_rect(topleft=(self.pos_x, self.pos_y))
                self.bloque.append(figura_rect)
                self.pos_y -= 20
class Bloque_6(Bloque):
    def __init__(self,screen,pos):
        super().__init__(screen,pos)
        self.figura.fill("orange")

    def crear_figura(self):
        if bool(self.bloque) == False:
            for i in range(2):
                figura_rect = self.figura.get_rect(topleft=(self.pos_x, self.pos_y))
                self.bloque.append(figura_rect)
                self.pos_x += 20
            self.pos_x -= 20
            self.pos_y += 20
            for i in range(2):
                figura_rect = self.figura.get_rect(topleft=(self.pos_x, self.pos_y))
                self.bloque.append(figura_rect)
                self.pos_x += 20
class Bloque_7(Bloque):
    def __init__(self,screen,pos):
        super().__init__(screen,pos)
        self.figura.fill("aqua")

    def crear_figura(self):
        if bool(self.bloque) == False:
            for i in range(2):
                figura_rect = self.figura.get_rect(topleft=(self.pos_x, self.pos_y))
                self.bloque.append(figura_rect)
                self.pos_x += 20
            self.pos_x -= 20
            self.pos_y -= 20
            for i in range(2):
                figura_rect = self.figura.get_rect(topleft=(self.pos_x, self.pos_y))
                self.bloque.append(figura_rect)
                self.pos_x += 20

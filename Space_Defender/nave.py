import copy

import pygame
class Nave():
    def __init__(self,screen,pos):
        self.screen = screen
        self.nave = pygame.Surface((10,10))
        self.nave.fill("lightgrey")
        self.pos_x = pos[0]
        self.pos_y = pos[1]


        self.rects = self.create_nave()

        self.shoot = pygame.Surface((8,15))
        self.shoot.fill("red")
        self.shoots = []
        self.pulsador = False

    def create_nave(self):
        rects = []
        matriz = [
            [0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1]
        ]
        for row_index,row in enumerate(matriz):
            for col_index, cell in enumerate(row):
                x = self.pos_x+col_index*10
                y = self.pos_y+row_index*10
                if cell == 1:
                    rect = self.nave.get_rect(topleft = (x,y))
                    rects.append(rect)
        rects[4].x += 5
        rects[8].x -= 5
        rects[9].x += 5
        rects[11].x -= 5

        return rects

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rects[4].x >= 10:
            for rect in self.rects:
                rect.x -= 10
        elif keys[pygame.K_RIGHT] and self.rects[8].x <= 580:
            for rect in self.rects:
                rect.x += 10
    def shooter(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and not self.pulsador:
            self.pulsador = True
            shoot_rect = copy.deepcopy(self.rects[0])
            shoot_rect.x += 2
            self.shoots.append(shoot_rect)

        for shoot in self.shoots:
            shoot.y -= 10
            if shoot.y < -40:
                self.shoots.remove(shoot)

        if not keys[pygame.K_SPACE]:
            self.pulsador = False

    def update(self):
        self.movement()
        self.shooter()

    def draw(self):
        for rect in self.rects:
            self.screen.blit(self.nave,rect)
        for shoot in self.shoots:
            self.screen.blit(self.shoot, shoot)


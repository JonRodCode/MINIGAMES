import pygame
from random import choice, randint

class Enemy():
    def __init__(self,screen,pos,vel):
        self.screen = screen
        self.tile = pygame.Surface((10,10))
        self.tile_color()
        self.pos = pos
        matriz = [
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 0]
        ]
        vel_min = vel[0]
        vel_max = vel[1]
        self.rects = self.create_enemy(matriz)
        self.speed = randint(vel_min,vel_max)
        self.speed_backup = 0

    def tile_color(self):
        colors = ["blue","darkgreen","aqua","yellow","darkviolet", "orange"]
        self.tile.fill(choice(colors))

    def create_enemy(self,matriz):
        rects = []
        for row_i,row in enumerate(matriz):
            for col_i,cell in enumerate(row):
                x = self.pos[0] + col_i*10
                y = self.pos[1] + row_i*10
                rect = self.tile.get_rect(topleft =(x,y))
                if cell == 1:
                    rects.append(rect)
        return rects

    def draw(self):
        for rect in self.rects:
            rect.y += self.speed
            self.screen.blit(self.tile,rect)

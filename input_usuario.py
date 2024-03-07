import pygame
import copy
import os, sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)
class Selector:
    def __init__(self, screen):
        self.pos_coord = [(200,330),(200,400),(400,330)]
        self.pos_actual = 2
        self.screen = screen
        self.button = False
    def shape_horizontal(self,n):
        cuad_line_horz = pygame.Surface((170, 5))
        cuad_line_horz.fill("darkgreen")
        cuad_line_horz_rect = cuad_line_horz.get_rect(center=self.pos_coord[n])
        dist_line_h = 65

        return cuad_line_horz, cuad_line_horz_rect, dist_line_h

    def shape_vertical(self,n):
        cuad_line_vert = pygame.Surface((5, 65))
        cuad_line_vert.fill("darkgreen")
        cuad_line_vert_rect = cuad_line_vert.get_rect(topleft=(self.pos_coord[n][0] - 85, self.pos_coord[n][1]))
        dist_line_v = 165

        return cuad_line_vert,cuad_line_vert_rect,dist_line_v
    def input_u(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and self.button == False:
            self.button = True
            if self.pos_actual != 1:
                self.pos_actual = 1

        elif keys[pygame.K_UP] and self.button == False:
            self.button = True
            if self.pos_actual == 1:
                self.pos_actual = 0

        elif keys[pygame.K_RIGHT] and self.button == False:
            self.button = True
            if self.pos_actual < 2:
                self.pos_actual = 2

        if keys[pygame.K_LEFT] and self.button == False:
            self.button = True
            if self.pos_actual == 2:
                self.pos_actual = 0

        else:
            self.button = False


        if keys[pygame.K_SPACE] and self.cuad_line_horz_rect.center == self.pos_coord[0]:
                exec(open(resource_path("Snake/main_Snake.py")).read())

        elif keys[pygame.K_SPACE] and self.cuad_line_horz_rect.center == self.pos_coord[1]:
                exec(open(resource_path("Tetris/main_tetris.py")).read())

        elif keys[pygame.K_SPACE] and self.cuad_line_horz_rect.center == self.pos_coord[2]:
                exec(open(resource_path("Space_Defender/main_Space_Defender.py")).read())
    def seleccionador(self):
        rect2 = copy.deepcopy(self.cuad_line_horz_rect)
        rect2.y = self.cuad_line_horz_rect.y + self.dist_line_h
        rect3 = copy.deepcopy(self.cuad_line_vert_rect)
        rect3.x = self.cuad_line_vert_rect.x + self.dist_line_v
        return rect2, rect3

    def draw(self):
        self.input_u()
        self.cuad_line_horz, self.cuad_line_horz_rect, self.dist_line_h, = self.shape_horizontal(self.pos_actual)
        self.cuad_line_vert, self.cuad_line_vert_rect, self.dist_line_v, = self.shape_vertical(self.pos_actual)

        rect2, rect3 = self.seleccionador()

        self.screen.blit(self.cuad_line_horz, self.cuad_line_horz_rect)
        self.screen.blit(self.cuad_line_horz, rect2)
        self.screen.blit(self.cuad_line_vert, self.cuad_line_vert_rect)
        self.screen.blit(self.cuad_line_vert, rect3)
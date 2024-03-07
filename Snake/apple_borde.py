import pygame
from random import randint

class Apple():
    def __init__(self,screen, tile_size):
        self.apple = pygame.Surface((tile_size, tile_size))
        self.apple.fill("red")
        self.rect = self.apple.get_rect(topleft = (randint(1,28)*tile_size,randint(4,28)*tile_size))
        self.screen = screen

    def draw(self):
        self.screen.blit(self.apple, self.rect)

class Borde():
    def __init__(self, screen):
        self.screen = screen
        self.wall = pygame.Surface((20, 540))
        self.wall.fill("darkgrey")
        self.ground_ceiling = pygame.Surface((600, 20))
        self.ground_ceiling.fill("darkgrey")

        self.wall_1_rect = self.wall.get_rect(topleft = (0,60))
        self.wall_2_rect = self.wall.get_rect(topleft=(580, 60))
        self.wall_3_rect = self.ground_ceiling.get_rect(topleft=(0, 60))
        self.wall_4_rect = self.ground_ceiling.get_rect(topleft=(0, 580))

        self.rect = [self.wall_1_rect,self.wall_2_rect,self.wall_3_rect,self.wall_4_rect] #esta lista esta hecha para Game_over()

    def draw(self):
        self.screen.blit(self.wall,self.wall_1_rect)
        self.screen.blit(self.wall, self.wall_2_rect)
        self.screen.blit(self.ground_ceiling, self.wall_3_rect)
        self.screen.blit(self.ground_ceiling, self.wall_4_rect)




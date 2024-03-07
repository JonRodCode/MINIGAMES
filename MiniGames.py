import pygame
import sys
from Textos import Draw_text
from settings import *
from input_usuario import Selector

pygame.init()
screen_size = 600,600
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("MINIJUEGOS")
clock = pygame.time.Clock()

game_on = True
minigames_active = False

selector = Selector(screen)
username = ""

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if not minigames_active:
            if event.type == pygame.KEYDOWN:
                username = Usuario(event.key, username)

    screen.fill("black")
    game_on = Game_over()
    if minigames_active:
        Draw_text(screen,username)
        selector.draw()
    else:
        minigames_active = Minigames_inactive(screen,username)

    pygame.display.update()
    clock.tick(20)
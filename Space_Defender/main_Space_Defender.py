import pygame
from Space_Defender.space import Space
from Space_Defender.settings import Salir, Game_over, Score, Game_inactive

pygame.init()
screen_size = (600,600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

game_on = True
game_active = False
space = Space(screen)

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("black")

    if game_active:
        space.draw()
        Score(space)
        game_active = Game_over(space)
    else:
        game_active = Game_inactive(space)
        if game_active == True:
            space = Space(screen)
    game_on = Salir()
    pygame.display.update()
    clock.tick(30)
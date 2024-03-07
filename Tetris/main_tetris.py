import pygame
from Tetris.bloques import *
from Tetris.game import Game
from Tetris.settings import screen_size, Salir, Game_inactive, Game_over, Score

pygame.init()
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
game_on = True
game_active = False
game = Game(screen)

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("black")

    if game_active:
        game.run()
        Score(game)
        game_active = Game_over(game)
    else:
        game_active = Game_inactive(game)
        if game_active == True:
            game = Game(screen)

    game_on = Salir()
    pygame.display.update()
    clock.tick(game.time_down())
import pygame
from collections import deque
from Snake.snake import Snake
from Snake.apple_borde import Apple
from Snake.settings import Salir, Game_over, Game_inactive, tile_size, Score, Aumentar_tiempo

pygame.init()
screen_size = (600,600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

game_on = True
game_active = False
manzana_list = deque()
snake = Snake(screen, manzana_list, tile_size)

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("black")
    if game_active:
        snake.draw()
        Score(snake)
        game_active = Game_over(snake)
    else:
        game_active = Game_inactive(snake)
        if game_active == True:
            manzana_list = deque()
            manzana_list.append(Apple(screen, tile_size))
            snake = Snake(screen, manzana_list, tile_size)
    game_on = Salir()
    pygame.display.update()
    clock.tick(Aumentar_tiempo(snake))
import pygame
import os, sys
from Snake.head_tail import Head, Tail
from Snake.apple_borde import Apple, Borde
from collections import deque

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)

class Snake():
    def __init__(self,screen, manzana_list,tile_size):
        self.snake = [Head(screen, tile_size)]
        self.apple_list = manzana_list
        self.screen = screen
        self.tile_size = tile_size

        self.score = 0
        self.pulsador_score = deque()

        self.borde = Borde(self.screen)

        for i in range(3):
            self.snake.append(Tail((self.snake[i].rect.topleft[0]-tile_size,self.snake[i].rect.topleft[1]),screen,tile_size))

    def game_score(self):
        for i in range(len(self.apple_list)):
            if self.snake[0].rect.colliderect(self.apple_list[i].rect) and len(self.apple_list) != len(self.pulsador_score):
                self.pulsador_score.append(True)
                if self.pulsador_score[i] == True:
                    self.score += 10
                    self.pulsador_score[i] = False
    def eat(self): # aca agregamos el metodo score
        self.game_score()
        if len(self.apple_list) > 0:
            for elem in self.apple_list:
                elem.draw()
            for i in range(len(self.apple_list)):
                if self.snake[0].rect.colliderect(self.apple_list[i].rect):
                    pos_manzana = self.apple_list[i].rect.center
                    if self.snake[0].rect.center == pos_manzana:
                        self.apple_list[i].apple.fill("green")
                        self.apple_list.append(Apple(self.screen,self.tile_size))
                        for i in range(len(self.snake)):
                            if self.apple_list[-1].rect.colliderect(self.snake[i].rect):
                                self.apple_list.pop()
                                self.apple_list.append(Apple(self.screen,self.tile_size))

            if len(self.apple_list) > 1:
                colision = 0
                for i in range(len(self.snake)):
                    if self.snake[i].rect.colliderect(self.apple_list[0].rect):
                        colision += 1
                if colision == 0:
                    pos_manzana = self.apple_list[0].rect.topleft
                    tail = Tail(pos_manzana,self.screen,self.tile_size)
                    tail.direction = self.snake[-1].direction
                    self.snake.append(tail)
                    self.apple_list.popleft()
                    self.pulsador_score.popleft()

    def clean_list_change(self):
        self.snake[-1].prev_dir_status.clear()
        self.snake[-1].snake_turn.clear()

    def tails_movement(self):
        if len(self.snake) > 1:
            for i in range(len(self.snake) - 1):
                if len(self.snake[i].snake_turn) > 0 and self.snake[i+1].rect.collidepoint(self.snake[i].snake_turn[0]):
                    self.snake[i+1].direction = self.snake[i].prev_dir_status[0][1]
                    self.snake[i].prev_dir_status.popleft()
                    self.snake[i].snake_turn.popleft()

    def pause_text(self):
        if self.snake[0].play_pause == "pause":
            font = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 100)
            text = font.render("Pause", True, "blue")
            text_rect = text.get_rect(center=(300, 250))
            bg = pygame.Surface((188,50))
            bg.fill("black")
            self.screen.blit(bg,text_rect)
            self.screen.blit(text, text_rect)

    def draw(self):
        self.borde.draw()
        self.eat()
        self.tails_movement()
        for elem in self.snake:
                elem.draw()
                self.screen.blit(self.snake[0].head,self.snake[0].rect)
                self.clean_list_change()
        self.pause_text()







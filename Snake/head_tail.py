import pygame
from collections import deque
class Head():
    def __init__(self,screen,tile_size):
        self.head = pygame.Surface((tile_size,tile_size))
        self.head.fill("darkgreen")
        self.rect = self.head.get_rect(topleft=(280,280))
        self.screen = screen

        #movimiento
        self.direction = pygame.math.Vector2(1,0)
        self.speed = 2
        self.len_move = 0

        #direccion
        self.dir_status = {"right": False, "left": False, "up": False, "down": False}

        #guardar info de cambio de direccion
        self.prev_dir_status = deque()
        self.snake_turn = deque()

        self.pulsador = False
        self.play_pause = "play"

    #Usuario input, determina el cambio de direccion si las condiciones son las indicadas
    def head_movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.len_move == 10 and self.dir_status["right"] != True:
            self.direction = pygame.math.Vector2(-1,0)
        if keys[pygame.K_RIGHT] and self.len_move == 10 and self.dir_status["left"] != True:
            self.direction = pygame.math.Vector2(1,0)
        if keys[pygame.K_UP] and self.len_move == 10 and self.dir_status["down"] != True:
            self.direction = pygame.math.Vector2(0,-1)
        if keys[pygame.K_DOWN] and self.len_move == 10 and self.dir_status["up"] != True:
            self.direction = pygame.math.Vector2(0,1)
    #Aplicacion de movimiento
    def movement(self):
        if self.len_move == 10:
            self.head_movement()
            self.len_move = 0
        self.rect.topleft += self.direction * self.speed
        self.len_move += 1
    #Si se hace un cambio de direccion, guardamos la direccion previa y la nueva direccion a girar para la cola
    def prev_direction_status(self):
        if self.direction.x == 1 and self.dir_status["right"] != True:
            direction_to_turn = pygame.math.Vector2(1, 0)
            for k in self.dir_status:
                if self.dir_status[k] == True:
                    self.prev_dir_status.append((k,direction_to_turn))
        if self.direction.x == -1 and self.dir_status["left"] != True:
            direction_to_turn = pygame.math.Vector2(-1, 0)
            for k in self.dir_status:
                if self.dir_status[k] == True:
                    self.prev_dir_status.append((k,direction_to_turn))
        if self.direction.y == 1 and self.dir_status["down"] != True:
            direction_to_turn = pygame.math.Vector2(0, 1)
            for k in self.dir_status:
                if self.dir_status[k] == True:
                    self.prev_dir_status.append((k,direction_to_turn))
        if self.direction.y == -1 and self.dir_status["up"] != True:
            direction_to_turn = pygame.math.Vector2(0, -1)
            for k in self.dir_status:
                if self.dir_status[k] == True:
                    self.prev_dir_status.append((k,direction_to_turn))
    #Determina el estado de la direccion actual
    def actual_direction_status(self):
        if self.direction.x == 1:
            for k in self.dir_status:
                if k != "right":
                    self.dir_status[k] = False
                else:
                    self.dir_status[k] = True
        if self.direction.x == -1:
            for k in self.dir_status:
                if k != "left":
                    self.dir_status[k] = False
                else:
                    self.dir_status[k] = True
        if self.direction.y == 1:
            for k in self.dir_status:
                if k != "down":
                    self.dir_status[k] = False
                else:
                    self.dir_status[k] = True
        if self.direction.y == -1:
            for k in self.dir_status:
                if k != "up":
                    self.dir_status[k] = False
                else:
                    self.dir_status[k] = True
    #Segun la direccion direccion actual y la previa, se guarda el punto de cambio de direccion para la cola
    def point_turn(self):
        if len(self.prev_dir_status) > 0 and len(self.prev_dir_status) != len(self.snake_turn):
            for k in self.dir_status:
                if k == "right" and self.dir_status[k] == True:
                    if self.prev_dir_status[-1][0] == "down":
                        self.snake_turn.append((self.rect.midbottom[0],self.rect.midbottom[1]-2))
                    elif self.prev_dir_status[-1][0] == "up":
                        self.snake_turn.append(self.rect.midtop)
                elif k == "left"  and self.dir_status[k] == True:
                    if self.prev_dir_status[-1][0] == "down":
                        self.snake_turn.append((self.rect.midbottom[0],self.rect.midbottom[1]-2))
                    elif self.prev_dir_status[-1][0] == "up":
                        self.snake_turn.append(self.rect.midtop)
                elif k == "down"  and self.dir_status[k] == True:
                    if self.prev_dir_status[-1][0] == "right":
                        self.snake_turn.append((self.rect.midright[0]-2,self.rect.midright[1]))
                    elif self.prev_dir_status[-1][0] == "left":
                        self.snake_turn.append((self.rect.midleft[0],self.rect.midleft[1]))
                elif k == "up"  and self.dir_status[k] == True:
                    if self.prev_dir_status[-1][0] == "right":
                        self.snake_turn.append((self.rect.midright[0]-2,self.rect.midright[1]))
                    elif self.prev_dir_status[-1][0] == "left":
                        self.snake_turn.append(self.rect.midleft)

    def game_pause(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p] and self.pulsador == False and self.play_pause == "play":
            self.pulsador = True
            self.play_pause = "pause"
            self.speed = 0

        elif keys[pygame.K_p] and self.pulsador == False and self.play_pause == "pause":
            self.pulsador = True
            self.play_pause = "play"
            self.speed = 2

        if not keys[pygame.K_p]:
            self.pulsador = False

    def play_game(self):
        if self.play_pause == "play":
            self.movement()

    def draw(self):
        self.game_pause()
        self.play_game()
        self.prev_direction_status()
        self.actual_direction_status()
        self.point_turn()
        self.screen.blit(self.head,self.rect)

class Tail(Head):
    def __init__(self, pos, screen, tile_size):
        super().__init__(screen,tile_size)
        self.tail = pygame.Surface((tile_size,tile_size))
        self.head.fill("green")
        self.rect = self.tail.get_rect(topleft=pos)
    def movement(self):
        self.rect.center += self.direction * self.speed
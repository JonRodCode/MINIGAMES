import copy
from random import randint
import os,sys
import pygame
from Space_Defender.nave import Nave
from Space_Defender.enemy import Enemy

tile_size = 10

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
class Space():
    def __init__(self,screen):
        self.screen = screen
        self.espacio = pygame.Surface((tile_size,tile_size))
        self.espacio.fill("white")
        self.nave = Nave(screen,(260,530))

        self.vel_max = 4
        self.enemigos = []

        self.pulsador = False

        self.enemies_pass = 0

        self.score = 0

        self.play_pause = "play"
    def reintegrar_enemies(self):
        while len(self.enemigos) < 10:
            self.enemigos = self.create_enemies(self.enemigos)

    def create_enemies(self,enemies_list):
        pos_x = randint(1, 57) * 10
        pos_y = randint(5, 20) * (-10)
        enemy = Enemy(self.screen, (pos_x, pos_y),(1,self.vel_max))
        collide = False
        for enemigo in enemies_list:
            for rect in enemigo.rects:
                for rect2 in enemy.rects:
                    if rect.colliderect(rect2):
                        collide = True
                        break
                if collide == True:
                    break
            if collide == True:
                break
        if not collide:
            enemies_list.append(enemy)
        return enemies_list

    def destroy_enemy(self):
        for enemy in self.enemigos:
            if enemy.rects[0].y > 650:
                self.enemigos.remove(enemy)
                self.enemies_pass +=1

    def shoot_collide(self):
        try:
            for shoot in self.nave.shoots:
                for enemy in self.enemigos:
                    for rect in enemy.rects:
                        if shoot.colliderect(rect):
                            c_collide = True
                            self.enemigos.remove(enemy)
                            self.nave.shoots.remove(shoot)
                            self.score += 1
        except:
            pass

    def Aumentar_dif(self):
        if self.score > 2000:
            self.vel_max = 10
        elif self.score > 1000:
            self.vel_max = 7
        elif self.score > 300:
            self.vel_max = 5
        else:
            self.vel_max = 4

    def pause_game(self): #Poner pausa en el juego
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p] and self.pulsador2 == False and self.play_pause == "play":
            self.pulsador2 = True
            self.play_pause = "pause"
            for enemy in self.enemigos:
                enemy.speed_backup = copy.copy(enemy.speed)
                enemy.speed = 0

        elif keys[pygame.K_p] and self.pulsador2 == False and self.play_pause == "pause":
            self.pulsador2 = True
            self.play_pause = "play"
            for enemy in self.enemigos:
                enemy.speed = enemy.speed_backup

        if not keys[pygame.K_p]:
            self.pulsador2 = False

    def enemies_pass_and_pause_text(self): #Si el estado del juego es pausa, ponemos el texto en pantalla
        if self.play_pause == "pause":
            font = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 100)
            text = font.render("Pause", True, "blue")
            text_rect = text.get_rect(center=(300, 250))
            bg = pygame.Surface((188,50))
            bg.fill("black")
            self.screen.blit(bg,text_rect)
            self.screen.blit(text, text_rect)

        font = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 40)
        text2 = font.render(f"Infiltrados:{self.enemies_pass}/10", True, "red")
        text2_size = text2.get_size()
        text2_bg = pygame.Surface(text2_size)
        text2_bg.fill("black")
        text2_rect = text2.get_rect(midtop = (300,20))
        self.screen.blit(text2_bg, text2_rect)
        self.screen.blit(text2, text2_rect)

    def play_game(self):
        if self.play_pause == "play":
            self.nave.update()

    def draw(self):
        self.destroy_enemy()
        self.reintegrar_enemies()
        self.nave.draw()
        self.shoot_collide()
        for enemy in self.enemigos:
            enemy.draw()
        self.Aumentar_dif()
        self.play_game()
        self.pause_game()
        self.enemies_pass_and_pause_text()





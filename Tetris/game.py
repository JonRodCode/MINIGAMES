import os,sys
import copy
import pygame.math
from random import choice
from Tetris.bloques import *
from Tetris.contenedor import Contenedor
from Tetris.settings import Aumentar_tiempo

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)
class Game():
    def __init__(self,screen):
        self.bloque_actual = []
        self.screen = screen
        self.speed = 5
        self.pulsador = False #giro
        self.pulsador2 = False #movimiento lateral bajada
        self.pulsador3 = False
        self.pulsador4 = False #play_pause
        self.contenedor = Contenedor(self.screen)
        self.pos = (280, 0)

        self.play_pause = "play"

    def crear_bloque(self): # crea un bloque aleatorio
        bloques = [Bloque_1(self.screen,self.pos), Bloque_2(self.screen,self.pos), Bloque_3(self.screen,self.pos),
                   Bloque_4(self.screen,self.pos), Bloque_5(self.screen,self.pos), Bloque_6(self.screen,self.pos),
                   Bloque_7(self.screen,self.pos)]

        if len(self.bloque_actual) < 1:
            self.bloque_actual.append(choice(bloques))

    def coleccion_floor(self): #Agrega el bloque actual al contenedor cuando colisione con el piso
        if len(self.bloque_actual) > 0:
            for i in range(4):
                if self.contenedor.floor_rect.colliderect(self.bloque_actual[0].bloque[i]):
                    self.contenedor.contenedor.append(self.bloque_actual[0])

                    #este for es para compensar el desplazamiento de colision por la velocidad

                    for j in range(4):
                        self.contenedor.contenedor[-1].bloque[j].y -= 5
                    self.bloque_actual.clear()
                    break
    def coleccion_contenedor(self): #Agrega el bloque actual al contenedor cuando colisione con algun bloque del contenedor
        if len(self.bloque_actual) > 0:
            for elem in self.contenedor.contenedor:
                for i in range(len(elem.bloque)):
                    for j in range(4):
                        if elem.bloque[i].colliderect(self.bloque_actual[0].bloque[j]):
                            self.contenedor.contenedor.append(self.bloque_actual[0])

                            #Este for es para compensar el desplzmiento por velocidad
                            for h in range(4):
                                self.contenedor.contenedor[-1].bloque[h].y -= 5
                            self.bloque_actual.clear()
                            break
                    if len(self.bloque_actual) == 0:
                        break
                if len(self.bloque_actual) == 0:
                    break

    def comp_colision(self,dist):
        """Este metodo comprueba si el bloque actual al girarlo, (usando el metodo "giro") en su nueva posicion colisiona
        con otro bloque que este dentro del contenedor, si lo hace lo desplaza hacia la izquierda o derecha. Por eso se
        pide un argumento dist"""
        c_colision = False
        for elemento in self.contenedor.contenedor:
            for i in range(len(elemento.bloque)):
                for j in range(4):
                    if elemento.bloque[i].colliderect(self.bloque_actual[0].bloque[j]):
                        c_colision = True
                        for i in range(4):
                            self.bloque_actual[0].bloque[i].x += dist
                        break
                if c_colision == True:
                    break
            if c_colision == True:
                break

    def comp_colision_final(self):
        """Este metodo comprueba si el bloque actual al girarlo, (usando el metodo "giro") en su nueva posicion colisiona
        con otro bloque que este dentro del contenedor, y retorna True o False"""
        for elemento in self.contenedor.contenedor:
            for i in range(len(elemento.bloque)):
                for j in range(4):
                    if elemento.bloque[i].colliderect(self.bloque_actual[0].bloque[j]):
                        return True
        return False
    def giro(self): #Este metodo usamos para girar el bloque actual
        keys = pygame.key.get_pressed()
        for elem in self.bloque_actual:
            if keys[pygame.K_SPACE] and self.pulsador == False:
                self.pulsador = True

                #Los Bloques 1,2 y 3 tienen 4 posiciones de giro

                if type(elem) == Bloque_1:
                    if elem.posicion == "1":
                        elem.posicion = "2"
                        elem.bloque[2].topleft += pygame.math.Vector2(-20,-20)

                    elif elem.posicion == "2":
                        elem.posicion = "3"
                        elem.bloque[0].y += 20
                        elem.bloque[2].topleft += pygame.math.Vector2(20,40)

                        self.comp_colision(-20) #desplazamos a la izquierda si colisiona con algun bloque

                        if elem.bloque[2].x >= 400: #desplazamos a la izquierda si supera el valor x de la pared derecha del contenedor
                            for i in range(4):
                                elem.bloque[i].x -= 20

                        c_colision = self.comp_colision_final()  #comprobamos que no choque con un bloque al desplazarlo (si es que lo hizo)

                        if elem.bloque[0].x <= 180: # comprobamos que la x no sea inferior a la de la pared izquierda del contenedor
                            c_colision = True

                        if c_colision == True:
                            #si choco con algo debemos cambiar a la posicion 4 ya que comparten la longitud en x con la posicion 2
                            elem.posicion = "4"
                            elem.bloque[0].topleft += pygame.math.Vector2(20, -40)
                            elem.bloque[2].y -= 20

                    elif elem.posicion == "3":
                        elem.posicion = "4"
                        elem.bloque[0].topleft += pygame.math.Vector2(20,-40)
                        elem.bloque[2].y -= 20
                    elif elem.posicion == "4":
                        elem.posicion = "1"
                        elem.bloque[0].topleft += pygame.math.Vector2(-20,20)

                        self.comp_colision(20) #desplazamos a la derecha si colisiona con algun bloque

                        if elem.bloque[0].x <= 180: #desplazamos a la derecha si es inferior o igual al valor x de la pared izquierda del...
                            for i in range(4):      #contenedor
                                elem.bloque[i].x += 20

                        c_colision = self.comp_colision_final() #comprobamos que no choque con un bloque al desplazarlo (si es que lo hizo)

                        if elem.bloque[2].x >= 400:# comprobamos que la x no supere a la de la pared derecha del contenedor
                            c_colision = True

                        if c_colision == True:
                            # si choco con algo debemos cambiar a la posicion 2 ya que comparten la longitud en x con la posicion 4
                            elem.posicion = "2"
                            elem.bloque[2].topleft += pygame.math.Vector2(-20, -20)

                elif type(elem) == Bloque_2:
                    if elem.posicion == "1":
                        elem.posicion = "2"
                        elem.bloque[0].topleft += pygame.math.Vector2(20,-20)
                        elem.bloque[2].topleft += pygame.math.Vector2(-20, 20)
                        elem.bloque[3].x -=40

                    elif elem.posicion == "2":
                        elem.posicion = "3"
                        elem.bloque[0].topleft += pygame.math.Vector2(-20, 20)
                        elem.bloque[1].topleft += pygame.math.Vector2(20, 20)

                        self.comp_colision(-20) #desplazamos a la izquierda si colisiona con algun bloque

                        if elem.bloque[1].x >= 400:
                            for i in range(4):
                                elem.bloque[i].x -= 20

                        c_colision = self.comp_colision_final() #comprobamos que no choque con un bloque al desplazarlo (si es que lo hizo)

                        if elem.bloque[3].x <= 180 or elem.bloque[0].x <= 180:
                            c_colision = True

                        if c_colision == True:
                            elem.posicion = "4"
                            elem.bloque[2].topleft += pygame.math.Vector2(0, -40)
                            elem.bloque[1].topleft += pygame.math.Vector2(0, -40)
                            elem.bloque[0].x += 20
                            elem.bloque[3].x += 20

                    elif elem.posicion == "3":
                        elem.posicion = "4"
                        elem.bloque[2].topleft += pygame.math.Vector2(-20,-40)
                        elem.bloque[1].topleft += pygame.math.Vector2(-20, -40)

                    elif elem.posicion == "4":
                        elem.posicion = "1"
                        elem.bloque[1].y += 20
                        elem.bloque[2].topleft += pygame.math.Vector2(40, 20)
                        elem.bloque[3].x += 40

                        self.comp_colision(-20) #desplazamos a la izquierda si colisiona con algun bloque

                        if elem.bloque[2].x >= 400:
                            for i in range(4):
                                elem.bloque[i].x -= 20

                        c_colision = self.comp_colision_final() #comprobamos que no choque con un bloque al desplazarlo (si es que lo hizo)

                        if elem.bloque[0].x <= 180:
                            c_colision = True

                        if c_colision == True:
                            elem.posicion = "2"
                            elem.bloque[0].topleft += pygame.math.Vector2(40, -20)
                            elem.bloque[1].x += 20
                            elem.bloque[2].y += 20
                            elem.bloque[3].x -= 20

                elif type(elem) == Bloque_3:
                    if elem.posicion == "1":
                        elem.posicion = "2"
                        elem.bloque[2].topleft += pygame.math.Vector2(-20, -20)
                        elem.bloque[1].topleft += pygame.math.Vector2(-20,-20)
                        elem.bloque[3].x += 20
                        elem.bloque[0].x += 20


                    elif elem.posicion == "2":
                        elem.posicion = "3"
                        elem.bloque[0].x += 20
                        elem.bloque[2].y += 40
                        elem.bloque[1].y += 40
                        elem.bloque[3].x += 20

                        self.comp_colision(-20) #desplazamos a la izquierda si colisiona con algun bloque

                        if elem.bloque[3].x >= 400: #movemos a la izquierda si choca con el muro derecho
                            for i in range(4):
                                elem.bloque[i].x -= 20

                        c_colision = self.comp_colision_final() #comprobamos que no choque con un bloque al desplazarlo (si es que lo hizo)

                        if elem.bloque[1].x <= 180:
                            c_colision = True

                        if c_colision == True:
                            elem.posicion = "4"
                            elem.bloque[1].x += 20
                            elem.bloque[0].x += -20
                            elem.bloque[2].topleft += pygame.math.Vector2(0, -40)

                    elif elem.posicion == "3":
                        elem.posicion = "4"
                        elem.bloque[3].x += -20
                        elem.bloque[0].x += -40
                        elem.bloque[2].topleft += pygame.math.Vector2(-20,-40)

                    elif elem.posicion == "4":
                        elem.posicion = "1"
                        elem.bloque[1].topleft += pygame.math.Vector2(20, -20)
                        elem.bloque[2].topleft += pygame.math.Vector2(40, 20)
                        elem.bloque[3].x -= 20

                        self.comp_colision(-20) #desplazamos a la izquierda si colisiona con algun bloque

                        if elem.bloque[2].x >= 400:  # movemos a la izquierda si choca con el muro derecho
                            for i in range(4):
                                elem.bloque[i].x -= 20

                        c_colision = self.comp_colision_final()  #comprobamos que no choque con un bloque al desplazarlo (si es que lo hizo)

                        if elem.bloque[0].x <= 180:
                            c_colision = True

                        if c_colision == True:
                            elem.posicion = "2"
                            elem.bloque[2].y -= 20
                            elem.bloque[1].y -= 20
                            elem.bloque[3].x += 40
                            elem.bloque[0].x += 40

                #Estos Bloques solo tienen 2 pos de giro
                elif type(elem) == Bloque_5:
                    #el bloque 5 tiene otro enfoque al girar, probablemente no es el mas optimo
                    if elem.posicion == "2":
                        elem.posicion = "1"
                        k = -20
                        for i in range(3):
                            elem.bloque[i+1].topleft += pygame.math.Vector2(k,k)
                            k -= 20

                    elif elem.posicion == "1":
                        surf = pygame.Surface((80,20)) #haremos pruebas con una superficie de reemplazo para comprobar
                        surf_rect = surf.get_rect(topleft =(elem.bloque[0].topleft))
                        c_colision = False
                        comprobador = 0
                        col_wall = False
                        pos_despl = 0

                        for i in range(3): # comprobamos si choca con el muro y desplazamos lo necesario para que entre
                            if surf_rect.colliderect(self.contenedor.wall_rect2):
                                surf_rect.x -=20
                                pos_despl += 20
                                col_wall = True

                        if col_wall == True: #comprobamos si choca con algun bloque al desplazarse
                            for elemento in self.contenedor.contenedor:
                                for i in range(len(elemento.bloque)):
                                    if elemento.bloque[i].colliderect(surf_rect):
                                        c_colision = True
                                        break
                                if c_colision == True:
                                    break

                        if c_colision != True: #movemos si colisiona con otro bloque
                            for elemento in self.contenedor.contenedor:
                                for i in range(len(elemento.bloque)):
                                    for j in range(3):
                                        if elemento.bloque[i].colliderect(surf_rect):
                                            surf_rect.x -= 20
                                            comprobador += 1
                                        if comprobador == 3:
                                            surf_rect.x -= 20
                                    if comprobador == 3:
                                        break
                                if comprobador == 3:
                                    break

                            for elemento in self.contenedor.contenedor: #confirmamos si choca con otro bloque al haberlo movido
                                for i in range(len(elemento.bloque)):
                                    if elemento.bloque[i].colliderect(surf_rect):
                                        c_colision = True

                            #comprobadores para desplazamiento si es que todo salio bien
                            if col_wall == True:
                                pos_despl = pos_despl
                            elif comprobador == 3:
                                pos_despl = 60
                            elif comprobador == 2:
                                pos_despl = 40
                            elif comprobador == 1:
                                pos_despl = 20
                            elif comprobador == 0:
                                pos_despl = 0
                            else:
                                c_colision = True

                            if surf_rect.colliderect(self.contenedor.wall_rect1): #confirmamos si choca el muro izquierdo al moverlo
                                c_colision = True

                        if c_colision == False: #si todo salio bien hacemos el movimiento
                            elem.posicion = "2"
                            k = 20
                            for i in range(3):
                                elem.bloque[i + 1].topleft += pygame.math.Vector2(k, k)
                                k += 20
                            for i in range(4):
                                elem.bloque[i].x -= pos_despl

                elif type(elem) == Bloque_6:
                    if elem.posicion == "1":
                        elem.posicion = "2"
                        elem.bloque[3].y -= 20
                        elem.bloque[0].topleft += pygame.math.Vector2(40,-20)

                    elif elem.posicion == "2":
                        resguardo = copy.deepcopy(elem.bloque)
                        elem.posicion = "1"
                        elem.bloque[3].y += 20
                        elem.bloque[0].topleft += pygame.math.Vector2(-40,20)

                        self.comp_colision(20) #movemos si choca con otro bloque

                        if elem.bloque[0].x <= 180: #movemos si choca con el borde
                            for i in range(4):
                                elem.bloque[i].x += 20

                        c_colision = self.comp_colision_final() #confirmamos que no choque con los bloques

                        if elem.bloque[3].x >= 400: #confirmamos que no choque con el borde
                            c_colision = True

                        if c_colision == True: #si se confirma no se puede girar, reemplazamos con el resguardo
                            elem.posicion = "2"
                            elem.bloque = resguardo

                elif type(elem) == Bloque_7:
                    if elem.posicion == "1":
                        elem.posicion = "2"
                        elem.bloque[3].x -= 40
                        elem.bloque[0].y -= 40

                    elif elem.posicion == "2":
                        resguardo = copy.deepcopy(elem.bloque)

                        elem.posicion = "1"
                        elem.bloque[3].x += 40
                        elem.bloque[0].y += 40

                        self.comp_colision(-20) #movemos si choca con otro bloque

                        if elem.bloque[3].x >= 400: #movemos si choca con el borde
                            for i in range(4):
                                elem.bloque[i].x -= 20

                        c_colision = self.comp_colision_final()  # confirmamos que no choque con los bloques

                        if elem.bloque[0].x <= 180: #confirmamos que no choque con el borde
                            c_colision = True

                        if c_colision == True: #si se confirma no se puede girar, reemplazamos con el resguardo
                            elem.posicion = "2"
                            elem.bloque = resguardo


        if not keys[pygame.K_SPACE]:
            self.pulsador = False

    def mov_lateral_bajada_auto(self):
        keys = pygame.key.get_pressed()
        left_pass = 0
        right_pass = 0
        c_colision = False #confirmador de colision
        c_desplazamiento = 0

        if len(self.bloque_actual) > 0:
            for i in range(4):              #confirmamos no salir del contenedor
                if self.bloque_actual[0].bloque[i].x <= 200:
                    left_pass +=1
                if self.bloque_actual[0].bloque[i].x >= 380:
                    right_pass += 1

            if keys[pygame.K_LEFT] and self.pulsador2 == False and left_pass == 0: #desplazamos hacia la izquierda
                self.pulsador2 = True
                for j in range(4):
                    self.bloque_actual[0].bloque[j].x -= 20 #desplazamos hacia la izquierda cada rect del bloque actual
                    c_desplazamiento += 1
                    for elem in self.contenedor.contenedor:
                        for i in range(len(elem.bloque)):
                            if elem.bloque[i].colliderect(self.bloque_actual[0].bloque[j]): #comprobamos que no chocamos con otro bloque
                                c_colision = True
                                for n in range(c_desplazamiento): #volvemos a desplazar el bloque actual a donde estaba
                                    self.bloque_actual[0].bloque[n].x += 20
                                break
                        if c_colision == True:
                            break
                    if c_colision == True:
                        break

            elif keys[pygame.K_RIGHT] and self.pulsador2 == False and right_pass == 0: #desplazamos a la derecha
                self.pulsador2 = True
                for j in range(4):
                    self.bloque_actual[0].bloque[j].x += 20 #desplazamos hacia la derecha cada rect del bloque actual
                    c_desplazamiento += 1
                    for elem in self.contenedor.contenedor:
                        for i in range(len(elem.bloque)):
                            if elem.bloque[i].colliderect(self.bloque_actual[0].bloque[j]):#comprobamos que no chocamos con otro bloque
                                c_colision = True
                                for n in range(c_desplazamiento): #volvemos a desplazar el bloque actual a donde estaba
                                    self.bloque_actual[0].bloque[n].x -= 20
                                break
                        if c_colision == True:
                            break
                    if c_colision == True:
                        break

        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.pulsador2 = False

        if keys[pygame.K_UP] and self.pulsador3 == False: #bajada de golpe del bloque
            self.pulsador3 = True
            while len(self.bloque_actual) == 1:
                for rect in self.bloque_actual[0].bloque:
                        rect.y += 5
                self.coleccion_floor()
                self.coleccion_contenedor()

        if not keys[pygame.K_UP]:
            self.pulsador3 = False

    def time_down(self): #esto es para la velocidad de bajada del bloque
        keys = pygame.key.get_pressed()
        tick = Aumentar_tiempo(self.contenedor)
        if keys[pygame.K_DOWN]:
            return tick * 3
        else:
            return tick


    def pause_game(self): #Poner pausa en el juego
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p] and self.pulsador4 == False and self.play_pause == "play":
            self.pulsador4 = True
            self.speed = 0
            self.play_pause = "pause"
        elif keys[pygame.K_p] and self.pulsador4 == False and self.play_pause == "pause":
            self.pulsador4 = True
            self.speed = 5
            self.play_pause = "play"

        if not keys[pygame.K_p]:
            self.pulsador4 = False
    def pause_text(self): #Si el estado del juego es pausa, ponemos el texto en pantalla
        if self.play_pause == "pause":
            font = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 100)
            text = font.render("Pause", True, "blue")
            text_rect = text.get_rect(center=(300, 250))
            bg = pygame.Surface((188,50))
            bg.fill("black")
            self.screen.blit(bg,text_rect)
            self.screen.blit(text, text_rect)
    def play_game(self): #Si el estado del juego es play, mantenemos los metodos de giro y mov. lateral
        if self.play_pause == "play":
            self.giro()
            self.mov_lateral_bajada_auto()

        for bloq in self.bloque_actual: #este for nos permite dar la velocidad de bajada al bloque actual
            for rect in bloq.bloque:
                rect.y += self.speed
            bloq.draw()

    def run(self):
        self.contenedor.draw()
        self.crear_bloque()
        self.coleccion_floor()
        self.coleccion_contenedor()
        self.pause_game()
        self.play_game()
        self.pause_text()

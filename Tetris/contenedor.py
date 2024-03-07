import copy
import pygame

class Contenedor:
    def __init__(self,screen):
        self.screen = screen

        self.wall = pygame.Surface((20,600))
        self.wall.fill("darkgrey")
        self.wall_rect1 = self.wall.get_rect(topleft = (180,0))
        self.wall_rect2 = self.wall.get_rect(topleft=(400, 0))
        self.floor = pygame.Surface((200,20))
        self.floor.fill("darkgrey")
        self.floor_rect = self.floor.get_rect(topleft = (200,580))

        self.contenedor = []
        self.score = 0

    def destructor(self): #si se completa una linea la destruye, mueve todo lo que este por encima y agrega puntos al score
        pos_y = 0
        for i in range(28): #esto es el tamaño en el eje y
            pos = (180, 560)
            pos += pygame.math.Vector2(0,pos_y)
            pos_y -= 20
            targets = [] #aca vamos a acumular las comprobaciones de rect en linea
            for i in range(10): #este for determina las 10 posiciones en el eje x del contenedor
                encontrado = False
                pos += pygame.math.Vector2(20, 0)
                for elemento in self.contenedor:
                    for i in range(len(elemento.bloque)):
                        if elemento.bloque[i].collidepoint(pos):
                            encontrado = True
                            pos_b = copy.copy(pos)
                            targets.append(pos_b)
                            break
                    if encontrado == True:
                        break

            if len(targets) == 10: #si target llega a 10 es porque completamos una linea (en x obvio)
                for target_pos in targets: #eliminamos cada rect de cada bloque que forme parte de la linea
                    borrado = False
                    for elemento in self.contenedor:
                        for i in range(len(elemento.bloque)):
                            if elemento.bloque[i].collidepoint(target_pos):
                                elemento.bloque.remove(elemento.bloque[i])
                                borrado = True
                                break
                        if borrado == True:
                            break

                self.quitar_bloques_vacios() #si borramos totalmente los rects de un bloque, eliminamos el bloque en si
                self.score += 10 #10 puntos por linea

                limite_y = targets[0][1] #tomamos la coord "y" donde se borro la linea, todo lo que esta por encima lo movemos hacia abajo
                for elemento in self.contenedor:
                    for rect in elemento.bloque:
                        if rect.y < limite_y:
                            rect.y += 20
    def quitar_bloques_vacios(self): # para eliminar bloques vacios
        for elem in self.contenedor:
            if len(elem.bloque) == 0:
                self.contenedor.remove(elem)

    def draw(self): #dibujamos las paredes, el piso del contenedor, los bloques contenidos y corremos el destructor
        self.screen.blit(self.wall,self.wall_rect1)
        self.screen.blit(self.wall, self.wall_rect2)
        self.screen.blit(self.floor,self.floor_rect)
        self.destructor()
        for i in range(len(self.contenedor)):
            self.contenedor[i].draw()
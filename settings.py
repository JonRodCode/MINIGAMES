import os, sys
import pygame
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)
def Usuario(event_key,username):
    if len(username) < 3:
        abecedario = {97: "A",
                          98: "B",
                          99: "C",
                          100: "D",
                          101: "E",
                          102: "F",
                          103: "G",
                          104: "H",
                          105: "I",
                          106: "J",
                          107: "K",
                          108: "L",
                          109: "M",
                          110: "N",
                          111: "O",
                          112: "P",
                          113: "Q",
                          114: "R",
                          115: "S",
                          116: "T",
                          117: "U",
                          118: "V",
                          119: "W",
                          120: "X",
                          121: "Y",
                          122: "Z"
                          }
        for key in abecedario:
            if key == event_key:
                username += abecedario[key]
    if event_key == 8:
        username = username[0:-1]
    return username
def Minigames_inactive(screen,username):
    font = pygame.font.Font(resource_path("Font\Pixeltype.ttf"), 70)
    text = font.render("Welcome to", None, "blue")
    text_rect = text.get_rect(center=(300, 90))
    screen.blit(text, text_rect)

    font2 = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 90)
    text2 = font2.render("MINIGAMES", None, "red")
    text2_rect = text2.get_rect(center=(300, 150))
    screen.blit(text2,text2_rect)

    font3 = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 50)
    text3 = font3.render("Please insert your name", None, "blue")
    text3_rect = text3.get_rect(center=(300, 250))
    screen.blit(text3, text3_rect)

    text4 = font3.render("Press ENTER to continue", None, "blue")
    text4_rect = text4.get_rect(center=(300, 500))
    screen.blit(text4, text4_rect)

    #posiciones tanto para las lineas como para las letras
    posiciones = [(235, 400), (300, 400), (365, 400)]

    # lineas bajo los carecteres de username
    linea = pygame.Surface((50, 5))
    linea.fill("darkgreen")
    linea_rect = linea.get_rect(center=posiciones[0])
    linea_rect2 = linea.get_rect(center=posiciones[1])
    linea_rect3 = linea.get_rect(center=posiciones[2])
    screen.blit(linea,linea_rect)
    screen.blit(linea, linea_rect2)
    screen.blit(linea, linea_rect3)

    #USERNAME
    for i in range(len(username)):
        letra = font.render(username[i],None,"orange")
        letra_rect = letra.get_rect(midbottom = posiciones[i])
        screen.blit(letra,letra_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN] and len(username) == 3:
        archivo = open(resource_path("actual_user.txt"), "w")
        archivo.write(username)
        archivo.close()

        if not os.path.isfile("Save_data/Users/"+username + ".txt"):
            archivo = open("Save_data/Users/"+username + ".txt", "a")
            archivo.write("0\n") #Snake
            archivo.write("0\n") #Tetris
            archivo.write("0")  #Space_Defender
            archivo.close()
        return True

    return False

def Game_over():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        return False
    return True


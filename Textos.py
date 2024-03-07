import pygame
import os, sys
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)
def Draw_text(screen,username):
    font = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 110)
    text = font.render("M I N I G A M E S", None, "red")
    text_rect = text.get_rect(center=(300, 100))
    screen.blit(text, text_rect)

    font2 = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 60)
    text2 = font2.render("Hi "+username+"!", None, "orange")
    text2_rect = text2.get_rect(center=(300, 200))
    screen.blit(text2, text2_rect)

    font3 = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 50)
    text3 = font3.render("Press SPACE to select a game", None, "blue")
    text3_rect = text3.get_rect(center=(300, 530))
    screen.blit(text3, text3_rect)

    #listado de juegos
    list_juegos = [["Snake","Tetris"],["Space Defender"]]
    font_2 = pygame.font.Font(resource_path(resource_path("Font/Pixeltype.ttf")), 50)
    pos_x = 200
    for i in range(len(list_juegos)):
        pos_y = 295
        for juego in list_juegos[i]:
            if " " in juego:
                juego = juego.split(" ")
                pos_y = 320
                for j in range(len(juego)):
                    juego_selec = font_2.render(juego[j], None, "blue")
                    pos_y += 30
                    juego_selec_rect = juego_selec.get_rect(center=(pos_x, pos_y))
                    screen.blit(juego_selec, juego_selec_rect)

            else:
                juego_selec = font_2.render(juego,None,"blue")
                pos_y += 70
                juego_selec_rect = juego_selec.get_rect(center = (pos_x,pos_y))
                screen.blit(juego_selec,juego_selec_rect)
        pos_x += 200 #esto nos va a permitir pasar al segundo listado





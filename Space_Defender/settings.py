import os,sys
import pygame
from Space_Defender.nave import Nave
from Space_Defender.enemy import Enemy
tile_size = 20

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)
def Salir():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_BACKSPACE]:
        return False
    return True

def Game_over(space):
    if space.enemies_pass >= 10:
        return False
    for rect in space.nave.rects:
        for enemigo in space.enemigos:
            for rect2 in enemigo.rects:
                if rect.colliderect(rect2):
                    return False
    return True

def Score(space):
    font = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 50)

    score = font.render("Score  " + str(space.score),None,"blue")
    score_size = score.get_size()
    score_bg = pygame.Surface(score_size)
    score_bg.fill("black")
    score_rect = score.get_rect(topright = (580,20))
    space.screen.blit(score_bg, score_rect)
    space.screen.blit(score, score_rect)

    archivo = open(resource_path("actual_user.txt"), "r")
    username = archivo.readline()
    archivo.close()

    user = font.render(username, None, "Orange")
    user_size = user.get_size()
    user_bg = pygame.Surface(user_size)
    user_bg.fill("black")
    user_rect = user.get_rect(topleft = (20,20))
    space.screen.blit(user_bg, user_rect)
    space.screen.blit(user,user_rect)

def Game_inactive(space):
    font = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 100)
    text = font.render("SPACE DEFENDER",None,"blue")
    text_rect = text.get_rect(center = (300,100))
    space.screen.blit(text, text_rect)

    font2 = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 50)

    text2 = font2.render("Press ENTER to start", None, "blue")
    text2_rect = text2.get_rect(center=(300, 490))
    space.screen.blit(text2, text2_rect)

    font3 = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 40)
    text3 = font3.render("Press RETURN to go back", None, "blue")
    text3_rect = text3.get_rect(center=(300, 540))
    space.screen.blit(text3, text3_rect)

    # Guardamos la variable del usuario actual
    archivo = open(resource_path("actual_user.txt"), "r")
    username = archivo.readline()
    archivo.close()

    # Buscamos los mejores puntajes
    best_score, best_user, user_best = Best_scores(space, username)

    user_score_text = font3.render(f"Your best score: {user_best}", None, "orange")
    user_score_text_rect = user_score_text.get_rect(center=(300, 330))
    space.screen.blit(user_score_text, user_score_text_rect)

    best_score_text = font3.render(f"Best score: {best_score} from {best_user}", None, "orange")
    best_score_text_rect = best_score_text.get_rect(center=(300, 430))
    space.screen.blit(best_score_text, best_score_text_rect)


    if len(space.enemigos) != 0:

        score_text = font2.render("Your score is: " + str(space.score), None, "orange")
        score_text_rect = score_text.get_rect(center=(300, 280))
        space.screen.blit(score_text, score_text_rect)

    else:
        text4 = font2.render("Hi "+username+"!", None, "Orange")
        text4_rect = text4.get_rect(center=(300, 280))
        space.screen.blit(text4, text4_rect)


        #dibujo de las naves
    display_surface = pygame.display.get_surface()
    nave = Nave(display_surface,(275,180))
    nave.draw()

    matriz = [
        [0, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

    colors = ["red", "darkgreen", "aqua", "yellow", "darkviolet", "orange"]
    pos_x = 380
    for i in range(3):
        enemigo = Enemy(display_surface,(pos_x,180),(0,0))
        enemigo.tile.fill(colors[i])
        enemigo.rects = enemigo.create_enemy(matriz)
        enemigo.draw()
        pos_x += 50

    matriz = [
        [1, 1, 0],
        [0, 1, 1],
        [1, 1, 0]
    ]
    pos_x = 190
    for i in range(3):
        enemigo = Enemy(display_surface,(pos_x,180),(0,0))
        enemigo.tile.fill(colors[i+3])
        enemigo.rects = enemigo.create_enemy(matriz)
        enemigo.draw()
        pos_x -= 50

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        return True
    return False

def Best_scores(space, username):
    # Leemos el mejor puntaje del juego y quien lo hizo
    archivo = open("Save_Data/Best_Scores/bs_space_defender.txt", "r+")
    best_score = archivo.readline().rstrip()
    best_user = archivo.readline()  # user con mejor puntaje
    archivo.seek(0)

    # Guardamos un nuevo mejor puntaje si es que lo hay
    if space.score > int(best_score):
        best_score = str(space.score) + "\n"
        archivo.write(best_score)
        archivo.write(username)
    archivo.close()

    # GUARDAMOS el mejor puntaje del usuario
    archivo2 = open(f"Save_Data/Users/{username}.txt", "r+")
    a1 = archivo2.readline().rstrip()
    a2 = archivo2.readline().rstrip()
    user_best = archivo2.readline().rstrip()

    if space.score > int(user_best):
        archivo2.seek(0)
        user_best = str(space.score)
        archivo2.write(a1 +"\n")
        archivo2.write(a2 +"\n")
        archivo2.write(user_best)
    archivo2.close()

    return best_score,best_user, user_best
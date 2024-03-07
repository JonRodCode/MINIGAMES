import pygame
import os,sys
from Tetris.bloques import *

tile_size = 20
screen_size = (600,600)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path,relative_path)

def Salir(): # Cerramos Tetris
    keys = pygame.key.get_pressed()
    if keys[pygame.K_BACKSPACE]:
        return False
    return True
def Game_over(game): # game over
    contenedor = game.contenedor.contenedor
    for elem in contenedor:
        for tile in elem.bloque:
            if tile.y < 5:
                return False
    return True
def Score(figura): #Nos muestra el Score actual mientras el juego esta activo
    font = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 50)
    # muestra la palabra score
    score_text = font.render("Score", None, "blue")
    score_text_rect = score_text.get_rect(center=(510, 60))
    figura.screen.blit(score_text, score_text_rect)

    # muestra el score actual
    score = font.render(str(figura.contenedor.score),None,"blue")
    score_rect = score.get_rect(center = (510,100))
    figura.screen.blit(score,score_rect)

    # muestra el nombre del usuario
    archivo = open(resource_path("actual_user.txt"), "r")
    username = archivo.readline()
    archivo.close()
    user = font.render(username, None, "Orange")
    user_rect = user.get_rect(center=(88, 60))
    figura.screen.blit(user, user_rect)
def Aumentar_tiempo(contenedor): #Aumenta la dificultad segun el score. esta en el mtd time_down de figura
    if contenedor.score >= 2500:
        return 75
    elif contenedor.score >= 500:
        return 50
    else:
        return 30
def Game_inactive(figura):
    font = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 100)
    text = font.render("TETRIS",None,"blue")
    text_rect = text.get_rect(center = (300,100))
    figura.screen.blit(text,text_rect)

    font2 = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 50)

    text2 = font2.render("Press ENTER to start", None, "blue")
    text2_rect = text2.get_rect(center=(300, 490))
    figura.screen.blit(text2, text2_rect)

    font3 = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 40)
    text3 = font3.render("Press RETURN to go back", None, "blue")
    text3_rect = text3.get_rect(center=(300, 540))
    figura.screen.blit(text3, text3_rect)

    # Guardamos la variable del usuario actual
    archivo = open(resource_path("actual_user.txt"), "r")
    username = archivo.readline()  # user actual
    archivo.close()

    # Buscamos los mejores puntajes
    best_score, best_user, user_best = Best_scores(figura, username)

    best_score_text = font3.render(f"Best score: {best_score} from {best_user}", None, "orange")
    best_score_text_rect = best_score_text.get_rect(center=(300, 430))
    figura.screen.blit(best_score_text, best_score_text_rect)

    user_score_text = font3.render(f"Your best score: {user_best}", None, "orange")
    user_score_text_rect = user_score_text.get_rect(center=(300, 330))
    figura.screen.blit(user_score_text, user_score_text_rect)

    if len(figura.contenedor.contenedor) != 0:
        score_text = font2.render("Your score is: " + str(figura.contenedor.score), None, "orange")
        score_text_rect = score_text.get_rect(center=(300, 280))
        figura.screen.blit(score_text, score_text_rect)

    else:
        text4 = font2.render("Hi "+ username+"!", None, "orange")
        text4_rect = text4.get_rect(center=(300, 280))
        figura.screen.blit(text4,text4_rect)

    y = 180
    bloques = [Bloque_1(figura.screen, (80,y)), Bloque_2(figura.screen, (210,y)), Bloque_3(figura.screen, (460,y)),
               Bloque_4(figura.screen, (290,y)), Bloque_5(figura.screen, (350,y+40)), Bloque_6(figura.screen, (150,y)),
               Bloque_7(figura.screen, (390,y+20))]
    for bloque in bloques:
        bloque.draw()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        return True
    return False

def Best_scores(figura,username):
    # Leemos el mejor puntaje del juego y quien lo hizo
    archivo = open("Save_data/Best_Scores/bs_tetris.txt", "r+")
    best_score = archivo.readline().rstrip()
    best_user = archivo.readline()  # user con mejor puntaje
    archivo.seek(0)

    # Guardamos un nuevo mejor puntaje si es que lo hay
    if figura.contenedor.score > int(best_score):
        best_score = str(figura.contenedor.score) + "\n"
        archivo.write(best_score)
        archivo.write(username)
    archivo.close()

    # GUARDAMOS el mejor puntaje del usuario
    archivo3 = open(f"Save_Data/Users/{username}.txt", "r+")
    a1 = archivo3.readline().rstrip()
    user_best = archivo3.readline().rstrip()
    a3 = archivo3.readline().rstrip()

    if figura.contenedor.score > int(user_best):
        archivo3.seek(0)
        user_best = str(figura.contenedor.score)
        archivo3.writelines(a1 + "\n")
        archivo3.write(user_best +"\n")
        archivo3.writelines(a3)
    archivo3.close()

    return best_score, best_user, user_best

import os,sys
import pygame
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

def Game_over(snake):
    if len(snake.snake) > 4: # Si choca con la cola
        for i in range(len(snake.snake)-4):
            if snake.snake[0].rect.colliderect(snake.snake[i+4]):
                return False

    for i in range(4): # Si choca con el borde
        if snake.snake[0].rect.colliderect(snake.borde.rect[i]):
            return False
    return True

def Score(snake):
    font = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 50)

    score = font.render("Score  " + str(snake.score),None,"blue")
    score_rect = score.get_rect(topright = (580,20))
    snake.screen.blit(score, score_rect)

    archivo = open(resource_path("actual_user.txt"), "r")
    username = archivo.readline()
    archivo.close()

    user = font.render(username, None, "Orange")
    user_rect = user.get_rect(topleft = (20,20))

    snake.screen.blit(user,user_rect)

def Aumentar_tiempo(snake): #Aumenta la dificultad segun el score
    if snake.score >= 2500:
        return 325
    elif snake.score >= 1500:
        return 250
    elif snake.score >= 900:
        return 200
    elif snake.score >= 500:
        return 150
    elif snake.score >= 200:
        return 125
    else:
        return 100

def Game_inactive(snake):
    font = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 100)
    text = font.render("SNAKE",None,"blue")
    text_rect = text.get_rect(center = (300,100))
    snake.screen.blit(text,text_rect)

    font2 = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 50)

    text2 = font2.render("Press ENTER to start", None, "blue")
    text2_rect = text2.get_rect(center=(300, 490))
    snake.screen.blit(text2, text2_rect)

    font3 = pygame.font.Font(resource_path("Font/Pixeltype.ttf"), 40)
    text3 = font3.render("Press RETURN to go back", None, "blue")
    text3_rect = text3.get_rect(center=(300, 540))
    snake.screen.blit(text3, text3_rect)

    # Guardamos la variable del usuario actual
    archivo = open(resource_path("actual_user.txt"), "r")
    username = archivo.readline()
    archivo.close()

    # Buscamos los mejores puntajes
    best_score, best_user, user_best = Best_scores(snake, username)

    user_score_text = font3.render(f"Your best score: {user_best}", None, "orange")
    user_score_text_rect = user_score_text.get_rect(center=(300, 330))
    snake.screen.blit(user_score_text, user_score_text_rect)

    best_score_text = font3.render(f"Best score: {best_score} from {best_user}", None, "orange")
    best_score_text_rect = best_score_text.get_rect(center=(300, 430))
    snake.screen.blit(best_score_text, best_score_text_rect)


    if len(snake.apple_list) != 0:

        score_text = font2.render("Your score is: " + str(snake.score), None, "orange")
        score_text_rect = score_text.get_rect(center=(300, 280))
        snake.screen.blit(score_text, score_text_rect)

    else:
        text4 = font2.render("Hi "+username+"!", None, "Orange")
        text4_rect = text4.get_rect(center=(300, 280))
        snake.screen.blit(text4,text4_rect)


        #dibujo de serpiente
    head = pygame.Surface((30, 30))
    head.fill("darkgreen")
    head_rect = head.get_rect(topleft = (330,180))
    snake.screen.blit(head, head_rect)

    tail = pygame.Surface((90, 30))
    tail.fill("green")
    tail_rect = tail.get_rect(topleft = (360,180))
    snake.screen.blit(tail, tail_rect)

    apple = pygame.Surface((30,30))
    apple.fill("red")
    apple_rect = apple.get_rect(topleft = (150,180))
    snake.screen.blit(apple, apple_rect)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        return True
    return False

def Best_scores(snake,username):
    # Leemos el mejor puntaje del juego y quien lo hizo
    archivo = open("Save_Data/Best_Scores/bs_snake.txt", "r+")
    best_score = archivo.readline().rstrip()
    best_user = archivo.readline()  # user con mejor puntaje
    archivo.seek(0)

    # Guardamos un nuevo mejor puntaje si es que lo hay
    if snake.score > int(best_score):
        best_score = str(snake.score) + "\n"
        archivo.write(best_score)
        archivo.write(username)
    archivo.close()

    # GUARDAMOS el mejor puntaje del usuario
    archivo2 = open(f"Save_Data/Users/{username}.txt", "r+")
    user_best = archivo2.readline().rstrip()
    a2 = archivo2.readline().rstrip()

    if snake.score > int(user_best):
        user_best = str(snake.score) + "\n"
        archivo2.seek(0)
        archivo2.write(user_best)
        archivo2.write(a2)
    archivo2.close()

    return best_score,best_user, user_best



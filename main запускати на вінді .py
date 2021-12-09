# importing libraries
import pickle

import pygame
import time
import random
import socket



my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.56.1"  # "127.0.1.1"
port = 7777
code = 1
my_socket.connect((host, port))


SNAKE_SPEED = 15

Run_status = True

# Window size
WINDOW_X = 720
WINDOW_Y = 480

# defining colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLUE = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snakes')
WINDOW = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

# FPS (frames per second) controller
FPS = pygame.time.Clock()

# defining snake default position
SNAKE_POS = [100, 50]

# defining first 4 blocks of snake body
SNAKE_BODY = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
FRUIT_POS = [random.randrange(1, (WINDOW_X // 10)) * 10,
             random.randrange(1, (WINDOW_Y // 10)) * 10]

FRUIT_SPAWN = True

# setting default snake direction towards
# right
DIRECTION = 'RIGHT'
change_to = DIRECTION

# initial SCORE
SCORE = 0


# displaying Score function
def show_score(choice, color, font, size):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(SCORE), True, color)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()

    # displaying text
    WINDOW.blit(score_surface, score_rect)


# game over function
def game_over():
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        'Your Score is : ' + str(SCORE), True, RED)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (WINDOW_X / 2, WINDOW_Y / 4)

    # blit wil draw the text on screen
    WINDOW.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(2)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()


# Main Function
while True :

    SNAKE_POS = SNAKE_POS or pickle.loads(my_socket.recv(1024))
    SNAKE_BODY = SNAKE_BODY or pickle.loads(my_socket.recv(1024))

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and DIRECTION != 'DOWN':
        DIRECTION = 'UP'
    if change_to == 'DOWN' and DIRECTION != 'UP':
        DIRECTION = 'DOWN'
    if change_to == 'LEFT' and DIRECTION != 'RIGHT':
        DIRECTION = 'LEFT'
    if change_to == 'RIGHT' and DIRECTION != 'LEFT':
        DIRECTION = 'RIGHT'

    # Moving the snake
    if DIRECTION == 'UP':
        SNAKE_POS[1] -= 10
    if DIRECTION == 'DOWN':
        SNAKE_POS[1] += 10
    if DIRECTION == 'LEFT':
        SNAKE_POS[0] -= 10
    if DIRECTION == 'RIGHT':
        SNAKE_POS[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    SNAKE_BODY.insert(0, list(SNAKE_POS))
    if SNAKE_POS[0] == FRUIT_POS[0] and SNAKE_POS[1] == FRUIT_POS[1]:
        SCORE += 1
        FRUIT_SPAWN = False
    else:
        SNAKE_BODY.pop()

    if not FRUIT_SPAWN:
        FRUIT_POS = [random.randrange(1, (WINDOW_X // 10)) * 10,
                     random.randrange(1, (WINDOW_Y // 10)) * 10]

    FRUIT_SPAWN = True
    WINDOW.fill(BLACK)

    for pos in SNAKE_BODY:
        pygame.draw.rect(WINDOW, GREEN,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(WINDOW, WHITE, pygame.Rect(
        FRUIT_POS[0], FRUIT_POS[1], 10, 10))

    # Game Over conditions
    if SNAKE_POS[0] > WINDOW_X - 10:
        game_over()

    if SNAKE_POS[1] < 0 or SNAKE_POS[1] > WINDOW_Y - 10:
        game_over()

    #Screan changing logic
    if SNAKE_POS[0] == -10:
        time_snake_postition = SNAKE_POS[0]   #тимчасова поз змії
        SNAKE_POS.insert(0, 710)
        SNAKE_POS.remove(SNAKE_POS[1])
        my_socket.send(pickle.dumps(SNAKE_POS))
        time.sleep(0.5)
        my_socket.send(pickle.dumps(SNAKE_BODY))
        SNAKE_POS.insert(0, time_snake_postition)
        SNAKE_POS.remove(SNAKE_POS[1])






    #Touching the snake body
    for block in SNAKE_BODY[1:]:
        if SNAKE_POS[0] == block[0] and SNAKE_POS[1] == block[1]:
            game_over()
    else:
        pass




    # displaying SCORE countinuously
    show_score(1, WHITE, 'times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refres Rate
    FPS.tick(SNAKE_SPEED)
    print(SNAKE_POS)

    #position reciving logic




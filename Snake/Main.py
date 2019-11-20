import pygame
import Snake.Classes
from pygame.locals import *
from Snake.Constants import *

pygame.init()

# Setting up the display
Screen = pygame.display.set_mode(DefaultResolution)

# Setting up the snake class
SnakePlayer = Snake.Classes.SnakeObject(Screen, 3)

LastKey = None
Spawn = False

# Defining the score and text
Score = 0
ScoreText = pygame.font.Font("Fonts/VT323-Regular.ttf", ScoreSize).render("Score = " + str(Score), True, White)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            elif event.key == K_LEFT:
                LastKey = "Left"
            elif event.key == K_RIGHT:
                LastKey = "Right"
            elif event.key == K_UP:
                LastKey = "Up"
            elif event.key == K_DOWN:
                LastKey = "Down"

    if 1 in pygame.key.get_pressed():
        GameSpeed = 100

    else:
        GameSpeed = 250

    Screen.fill(Black)

    if LastKey is None:
        SnakePlayer.Draw()

    else:
        SnakePlayer.Update(LastKey)

    if Spawn is not False:
        if SnakePlayer.Head.colliderect(Block):
            Spawn = False
            SnakePlayer.Collision()
            SnakePlayer.Update(LastKey)

            Score += 1
            ScoreText = pygame.font.Font("Fonts/VT323-Regular.ttf", ScoreSize).render("Score = " + str(Score), True,
                                                                                      White)
    if SnakePlayer.Head.collidelistall(SnakePlayer.Body):
        SnakePlayer = Snake.Classes.SnakeObject(Screen, 3)
        LastKey = None

    if Spawn is False:
        Block = Snake.Classes.BlockObject().Spawn()
        Spawn = True

    Screen.blit(ScoreText, (0, 0))
    pygame.draw.rect(Screen, Red, Block)
    pygame.display.flip()
    pygame.time.wait(GameSpeed)

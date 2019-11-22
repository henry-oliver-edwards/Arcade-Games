import pygame
import SpaceInvaders.Classes
from SpaceInvaders.Constants import *
from pygame.locals import *

pygame.init()

# Setting up the display
Screen = pygame.display.set_mode(DefaultResolution)

# Setting up the player class
Player = SpaceInvaders.Classes.PlayerObject("Images/Ship.png", Screen)

# Settling up the bullet class
Bullet = SpaceInvaders.Classes.BulletObject(Player.x, BulletHeight, BulletWidth, Screen)

# Setting up the alien classes
Alien1 = SpaceInvaders.Classes.AlienObject("Images/Alien 1.png", Screen)
Alien2 = SpaceInvaders.Classes.AlienObject("Images/Alien 2 Green.png", Screen)
Alien3 = SpaceInvaders.Classes.AlienObject("Images/Alien 3 Red.png", Screen)
Alien4 = SpaceInvaders.Classes.AlienObject("Images/Alien 4 Blue.png", Screen)
Alien5 = SpaceInvaders.Classes.AlienObject("Images/Alien 5 Yellow.png", Screen)
Alien6 = SpaceInvaders.Classes.AlienObject("Images/Alien 6 Light Blue.png", Screen)
Alien7 = SpaceInvaders.Classes.AlienObject("Images/Alien 7 Magenta.png", Screen)
Alien8 = SpaceInvaders.Classes.AlienObject("Images/Alien 8 Orange.png", Screen)
Alien9 = SpaceInvaders.Classes.AlienObject("Images/Alien 9 Purple.png", Screen)

SpawnAlien = True
AlienList = []
AlienCount = 1
Round = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            if event.key == K_UP:
                if Bullet.Spawn is False:
                    Bullet = SpaceInvaders.Classes.BulletObject(Player.x, BulletHeight, BulletWidth, Screen)
                    Bullet.Spawn = True

    Screen.fill(Black)
    KeysPressed = pygame.key.get_pressed()

    if SpawnAlien is True:

        if len(AlienList) > 0:
            if AlienList[0].x % 64 == 0:
                if AlienCount == 1:
                    AlienList.append(Alien1)
                    AlienCount += 1
                    Alien1 = SpaceInvaders.Classes.AlienObject("Images/Alien 1.png", Screen)
                elif AlienCount == 2:
                    AlienList.append(Alien2)
                    AlienCount += 1
                    Alien2 = SpaceInvaders.Classes.AlienObject("Images/Alien 2 Green.png", Screen)
                elif AlienCount == 3:
                    AlienList.append(Alien3)
                    AlienCount += 1
                    Alien3 = SpaceInvaders.Classes.AlienObject("Images/Alien 3 Red.png", Screen)
                elif AlienCount == 4:
                    AlienList.append(Alien4)
                    AlienCount += 1
                    Alien4 = SpaceInvaders.Classes.AlienObject("Images/Alien 4 Blue.png", Screen)
                elif AlienCount == 5:
                    AlienList.append(Alien5)
                    AlienCount += 1
                    Alien5 = SpaceInvaders.Classes.AlienObject("Images/Alien 5 Yellow.png", Screen)
                elif AlienCount == 6:
                    AlienList.append(Alien6)
                    AlienCount += 1
                    Alien6 = SpaceInvaders.Classes.AlienObject("Images/Alien 6 Light Blue.png", Screen)
                elif AlienCount == 7:
                    AlienList.append(Alien7)
                    AlienCount += 1
                    Alien7 = SpaceInvaders.Classes.AlienObject("Images/Alien 7 Magenta.png", Screen)
                elif AlienCount == 8:
                    AlienList.append(Alien8)
                    AlienCount += 1
                    Alien8 = SpaceInvaders.Classes.AlienObject("Images/Alien 8 Orange.png", Screen)
                elif AlienCount == 9:
                    AlienList.append(Alien9)
                    AlienCount += 1
                    Alien9 = SpaceInvaders.Classes.AlienObject("Images/Alien 9 Purple.png", Screen)

        elif not AlienList:
            AlienList.append(Alien1)
            AlienCount += 1
            Alien1 = SpaceInvaders.Classes.AlienObject("Images/Alien 1.png", Screen)

    if (len(AlienList)) % (5 * Round) == 0:
        SpawnAlien = False

    if AlienCount == 10:
        AlienCount = 1

    if KeysPressed[K_LEFT]:
        Player.Update("Left")
    elif KeysPressed[K_RIGHT]:
        Player.Update("Right")
    else:
        Player.Update(None)

    for Alien in AlienList:
        Alien.Update()
        if Bullet.Spawn:
            if Alien.colliderect(Bullet):
                AlienList.remove(Alien)
                AlienCount -= 1
                Bullet.Spawn = False

    if len(AlienList) == 0:
        AlienCount = 1
        Round += 1
        SpawnAlien = True
        Alien1 = SpaceInvaders.Classes.AlienObject("Images/Alien 1.png", Screen)
        Alien2 = SpaceInvaders.Classes.AlienObject("Images/Alien 2 Green.png", Screen)
        Alien3 = SpaceInvaders.Classes.AlienObject("Images/Alien 3 Red.png", Screen)
        Alien4 = SpaceInvaders.Classes.AlienObject("Images/Alien 4 Blue.png", Screen)
        Alien5 = SpaceInvaders.Classes.AlienObject("Images/Alien 5 Yellow.png", Screen)
        Alien6 = SpaceInvaders.Classes.AlienObject("Images/Alien 6 Light Blue.png", Screen)
        Alien7 = SpaceInvaders.Classes.AlienObject("Images/Alien 7 Magenta.png", Screen)
        Alien8 = SpaceInvaders.Classes.AlienObject("Images/Alien 8 Orange.png", Screen)
        Alien9 = SpaceInvaders.Classes.AlienObject("Images/Alien 9 Purple.png", Screen)

    Bullet.Update()
    pygame.display.flip()

import pygame
from SpaceInvaders.Constants import *


class PlayerObject:

    def __init__(self, PlayerImage, Surface):
        self.Image = pygame.image.load(PlayerImage)
        self.Screen = Surface
        self.x = (DefaultResolution[0] / 2) - (ImageWidth / 2)
        self.y = DefaultResolution[1] - ImageHeight
        self.NumberOfBullets = 0
        self.Bullet = None

    def Draw(self):
        self.Screen.blit(self.Image, (self.x, self.y))

    def Update(self, Direction):
        if Direction is "Left":
            self.x -= 2
        elif Direction is "Right":
            self.x += 2
        elif Direction is None:
            pass

        self.Draw()


class BulletObject(pygame.Rect):

    def __init__(self, x, Height, Width, Surface, *args, **kwargs):
        self.x = x + (ImageWidth / 2)
        self.y = DefaultResolution[1] - ImageHeight
        self.Height = Height
        self.Width = Width
        self.Screen = Surface
        self.Bullet = pygame.Rect(self.x, self.y, self.Width, self.Height)
        self.Spawn = False

        super().__init__(self.Bullet)

    def Draw(self):
        self.Bullet = pygame.Rect(self.x, self.y, self.Width, self.Height)
        pygame.draw.rect(self.Screen, White, self.Bullet)
        if self.y < 0:
            self.Spawn = False

    def Update(self):
        if self.Spawn is True:
            self.y -= 2
            self.Draw()


class AlienObject(pygame.Rect):

    def __init__(self, AlienImage, Surface, *args, **kwargs):

        self.x = 0
        self.y = 0
        self.Image = pygame.image.load(AlienImage)
        self.Rect = self.Image.get_rect()
        self.Direction = "Right"
        self.Screen = Surface

        super().__init__(self.Rect)

    def Draw(self):
        self.Screen.blit(self.Image, (self.x, self.y))

    def Update(self):
        if self.Direction == "Right":
            self.x += 1
        elif self.Direction == "Left":
            self.x -= 1

        if self.x > DefaultResolution[0] - 33:
            self.y += 43
            self.Direction = "Left"
        elif self.x < 0:
            self.y += 43
            self.Direction = "Right"

        self.Rect = self.Image.get_rect()
        self.Draw()


import pygame
from Snake.Constants import *
from random import randint


class SnakeObject:

    def __init__(self, Surface, Size):
        # Defines the initial starting size and screen to draw to
        self.Size = Size
        self.Screen = Surface

        # Lists to keep track of snake position and a dictionary to map these positions to individual units
        self.x = []
        self.y = []
        self.Position = {}

        # For loops to generate the starting positions of the snake segments given
        for _ in range(self.Size):
            self.x.append(DefaultResolution[0]/2 + (_ * (SnakeWidth + SnakeGap)))

        for _ in range(self.Size):
            self.y.append(DefaultResolution[1]/2)

        for _ in range(self.Size):
            self.Position[_] = [self.x[_], self.y[_]]

        # Head and body variables for collision detection, redefined later, just declared here
        self.Head = pygame.Rect((self.x[0], self.y[0]), (SnakeWidth, SnakeWidth))
        self.Body = []

    def Draw(self):
        for _ in self.Position.values():
            if _ == self.Position[0]:
                pygame.draw.rect(self.Screen, DarkerGreen, (_, (SnakeWidth, SnakeHeight)))
            else:
                pygame.draw.rect(self.Screen, Green, (_, (SnakeWidth, SnakeHeight)))

    @staticmethod
    def Rotate(List, n):
        return List[-n:] + List[:-n]

    def Collision(self):
        self.Size += 1
        self.x.append(self.x[self.Size - 2])
        self.y.append(self.y[self.Size - 2])

    def Update(self, Key):
        self.x = self.Rotate(self.x, 1)
        self.y = self.Rotate(self.y, 1)

        self.x[0] = self.x[1]
        self.y[0] = self.y[1]

        if Key == "Left":
            self.x[0] -= SnakeWidth + SnakeGap

        if Key == "Right":
            self.x[0] += SnakeWidth + SnakeGap

        if Key == "Up":
            self.y[0] -= SnakeWidth + SnakeGap

        if Key == "Down":
            self.y[0] += SnakeWidth + SnakeGap

        for _ in range(self.Size):
            self.Position[_] = [self.x[_], self.y[_]]

        self.Head = pygame.Rect((self.x[0], self.y[0]), (SnakeWidth, SnakeHeight))

        self.Body = []
        for _ in range(1, self.Size):
            self.Body.append(pygame.Rect((self.x[_], self.y[_]), (SnakeWidth, SnakeHeight)))

        self.Draw()


class BlockObject:

    def Spawn(self):
        x = randint(0, DefaultResolution[0] - SnakeWidth)
        y = randint(0, DefaultResolution[1] - SnakeHeight)

        while x % 15 != 0:
            x = randint(0, DefaultResolution[0] - SnakeWidth)

        while y % 15 != 0:
            y = randint(0, DefaultResolution[1] - SnakeHeight)

        return pygame.Rect((x, y), (SnakeWidth, SnakeHeight))






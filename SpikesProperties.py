import pygame
import random
from Menus import GameMenuProperties

screenProperties = GameMenuProperties.GameMenuProperties()


class LeftSpike:
    colorR = 255
    colorG = 255
    colorB = 255
    spikeColor = (colorR, colorG, colorB)

    width = 50
    height = 30

    positionX = 0
    positionY = random.randrange(0, screenProperties.height - height)

    def refreshPositionY(self):
        self.positionY = random.randrange(0, screenProperties.height - self.height)

    def setColorR(self, newColor):
        self.colorR = newColor

    def setColorG(self, newColor):
        self.colorG = newColor

    def setColorB(self, newColor):
        self.colorB = newColor

    def setPositionX(self, newPositionX):
        self.positionX = newPositionX

    def createSpike(self, screen):
        return pygame.draw.polygon(
            screen,
            self.spikeColor,
            [[self.positionX, self.positionY],
             [self.positionX, self.positionY + self.height],
             [self.positionX + self.width,
              (self.positionY + self.positionY + self.height) / 2]]
        )


class RightSpike(LeftSpike):
    screenProperties = GameMenuProperties.GameMenuProperties()

    positionX = screenProperties.width

    def createSpike(self, screen):
        return pygame.draw.polygon(
            screen,
            self.spikeColor,
            [[self.positionX, self.positionY],
             [self.positionX, self.positionY + self.height],
             [self.positionX - self.width,
              (self.positionY + self.positionY + self.height) / 2]]
        )

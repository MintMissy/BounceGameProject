class Spike:
    import random
    import ScreenProperties
    screenProperties = ScreenProperties.ScreenProperties()

    colorR = 255
    colorG = 255
    colorB = 255
    spikeColor = (colorR, colorG, colorB)

    width = 50
    height = 30

    positionX = 0
    positionY = random.randrange(0, screenProperties.height)

    def setColorR(self, newColor):
        self.colorR = newColor

    def setColorG(self, newColor):
        self.colorG = newColor

    def setColorB(self, newColor):
        self.colorB = newColor

    def setPositionX(self, newPositionX):
        self.positionX = newPositionX

    def setPositionY(self, newPositionY):
        self.positionY = newPositionY


class RightSpike(Spike):
    import ScreenProperties
    screenProperties = ScreenProperties.ScreenProperties()

    positionX = screenProperties.width


class LeftSpike(Spike):
    positionX = 0

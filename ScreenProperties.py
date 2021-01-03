class ScreenProperties:
    width = 800
    height = 600

    colorR = 48
    colorG = 48
    colorB = 54
    screenColor = (colorR, colorG, colorB)

    def getCenterX(self):
        return self.width / 2

    def getCenterY(self):
        return self.height / 2


    def getColor(self):
        return self.screenColor

    def setColorR(self, newColor):
        self.colorR = newColor

    def setColorG(self, newColor):
        self.colorR = newColor

    def setColorB(self, newColor):
        self.colorR = newColor

    # TODO Method for dynamic colors on screen
    def dynamicColors(self, colorType):
        # Check if increase color value or decrease
        increaseColor = True
        if self.colorR == 255:
            increaseColor = False
        if self.colorR == 0:
            increaseColor = True

        # Increase of decrease color value
        if increaseColor:
            self.colorR += 1
        else:
            self.colorR -= 1

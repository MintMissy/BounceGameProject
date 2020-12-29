class ScreenProperties:
    width = 800
    height = 600
    centerX = width / 2
    centerY = height / 2

    colorR = 218
    colorG = 245
    colorB = 244
    screenColor = (colorR, colorG, colorB)

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getCenterX(self):
        return self.centerX

    def getCenterY(self):
        return self.centerY


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

class MenuProperties:
    colorType = 1
    width = 1500
    height = 900

    colorR = 45
    colorG = 237
    colorB = 53
    screenColor = (colorR, colorG, colorB)

    def getCenterX(self):
        return self.width / 2

    def getCenterY(self):
        return self.height / 2

    def setColorType(self, newColorType):
        self.colorType = newColorType

    def setColors(self, newColorR, newColorG, newColorB):
        self.colorR = newColorR
        self.colorG = newColorG
        self.colorB = newColorB

    def setColorR(self, newColor):
        self.colorR = newColor

    def setColorG(self, newColor):
        self.colorR = newColor

    def setColorB(self, newColor):
        self.colorR = newColor

    def refreshScreenColors(self):
        self.screenColor = (self.colorR, self.colorG, self.colorB)

    def dynamicColors(self, colorMultiplier):
        if self.colorType == 0:
            if self.colorR == 45 - colorMultiplier:
                self.colorType = 1
            else:
                self.colorR -= 1
        if self.colorType == 1:
            if self.colorB == 237 - colorMultiplier:
                self.colorType = 2
            else:
                self.colorB += 1
        if self.colorType == 2:
            if self.colorG == 45 - colorMultiplier:
                self.colorType = 3
            else:
                self.colorG -= 1
        if self.colorType == 3:
            if self.colorR == 237 - colorMultiplier:
                self.colorType = 4
            else:
                self.colorR += 1
        if self.colorType == 4:
            if self.colorB == 45 - colorMultiplier:
                self.colorType = 5
            else:
                self.colorB -= 1
        if self.colorType == 5:
            if self.colorG == 237 - colorMultiplier:
                self.colorType = 0
            else:
                self.colorG += 1

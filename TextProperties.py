class Text:
    font = 'Fonts/8-BIT WONDER.TTF'

    colorType = 0

    size = 100

    colorR = 255
    colorG = 255
    colorB = 64
    textColor = (colorR, colorG, colorB)

    def setSize(self, newSize):
        self.size = newSize

    def setFont(self, newFont):
        self.font = newFont

    def refreshColor(self):
        self.textColor = (self.colorR, self.colorG, self.colorB)

    def setColorType(self, newColorType):
        self.colorType = newColorType

    def setColors(self, newColorR, newColorG, newColorB):
        self.colorR = newColorR
        self.colorG = newColorG
        self.colorB = newColorB

    def setColorR(self, newColor):
        self.colorR = newColor

    def setColorG(self, newColor):
        self.colorG = newColor

    def setColorB(self, newColor):
        self.colorB = newColor

    def dynamicColors(self , colorMultiplier):
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

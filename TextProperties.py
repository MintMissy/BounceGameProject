class Text:
    font = 'Fonts/8-BIT WONDER.TTF'

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

    def setColorR(self, newColor):
        self.colorR = newColor

    def setColorG(self, newColor):
        self.colorG = newColor

    def setColorB(self, newColor):
        self.colorB = newColor

import Menus.MenuProperties as MenuProperties


class StartMenuProperties(MenuProperties.MenuProperties):
    gameStart = False

    colorR = 45
    colorG = 237
    colorB = 53
    screenColor = (colorR, colorG, colorB)

    buttonColorR = 255
    buttonColorG = 255
    buttonColorB = 255
    buttonColor = (buttonColorR, buttonColorG, buttonColorB)

    buttonShadeColorR = 200
    buttonShadeColorG = 200
    buttonShadeColorB = 200
    buttonShadeColor = (buttonColorR, buttonColorG, buttonColorB)

    def setButtonColorR(self, newColor):
        self.buttonColorR = newColor

    def setButtonColorG(self, newColor):
        self.buttonColorG = newColor

    def setButtonColorB(self, newColor):
        self.buttonColorB = newColor

    def setButtonShadeColorR(self, newColor):
        self.buttonShadeColorR = newColor

    def setButtonShadeColorG(self, newColor):
        self.buttonShadeColorG = newColor

    def setButtonShadeColorB(self, newColor):
        self.buttonShadeColorB = newColor

    def setGameStart(self, newGameStart):
        self.gameStart = newGameStart

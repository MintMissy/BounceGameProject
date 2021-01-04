import Menus.MenuProperties as MenuProperties


class StartMenuProperties(MenuProperties.MenuProperties):
    gameStart = False

    colorR = 55
    colorG = 55
    colorB = 66

    def setGameStart(self, newGameStart):
        self.gameStart = newGameStart

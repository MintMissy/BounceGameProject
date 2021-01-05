import Menus.MenuProperties as MenuProperties


class GameMenuProperties(MenuProperties.MenuProperties):
    colorType = 1
    colorR = 45
    colorG = 237
    colorB = 53

    def refreshScreenColors(self):
        self.screenColor = (self.colorR, self.colorG, self.colorB)

    def dynamicColors(self):
        if self.colorType == 0:
            if self.colorR == 45:
                self.colorType = 1
            else:
                self.colorR -= 1
        if self.colorType == 1:
            if self.colorB == 237:
                self.colorType = 2
            else:
                self.colorB += 1
        if self.colorType == 2:
            if self.colorG == 45:
                self.colorType = 3
            else:
                self.colorG -= 1
        if self.colorType == 3:
            if self.colorR == 237:
                self.colorType = 4
            else:
                self.colorR += 1
        if self.colorType == 4:
            if self.colorB == 45:
                self.colorType = 5
            else:
                self.colorB -= 1
        if self.colorType == 5:
            if self.colorG == 237:
                self.colorType = 0
            else:
                self.colorG += 1

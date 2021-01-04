import Menus.MenuProperties as MenuProperties


class GameMenuProperties(MenuProperties.MenuProperties):

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

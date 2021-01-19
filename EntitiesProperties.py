class EntityVector:
    import Menus.GameMenuProperties as GameMenuProperties

    screenProperties = GameMenuProperties.GameMenuProperties()

    colorR = 255
    colorG = 255
    colorB = 230
    entityColor = (colorR, colorG, colorB)

    defaultSize = 30
    size = 30
    speed = screenProperties.width / 110
    defaultSpeed = screenProperties.width / 110
    gravitySpeed = screenProperties.height / 230
    defaultGravity = screenProperties.height / 230
    defaultJumpHeight = -screenProperties.height / 65
    alive = True

    positionX = screenProperties.getCenterX()
    positionY = screenProperties.getCenterY()

    bounceRight = True

    def setAlive(self, newAlive):
        self.alive = newAlive

    def setSpeed(self, newSpeed):
        self.speed = newSpeed

    def setGravity(self, newGravity):
        self.gravitySpeed = newGravity

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

    # If true bounce right
    def setBounce(self, newBounce):
        self.bounceRight = newBounce

    def setSize(self, newSize):
        self.size = newSize


class EntityCircle(EntityVector):
    # is circle
    a = 5


class EntitySquare(EntityVector):
    b = 5


class EntityGraphic():
    size = 20

    speed = 3
    gravitySpeed = 50

    positionX = 100
    positionY = 100

    bounceRight = True

    def setGravity(self, newGravity):
        self.gravitySpeed = newGravity

    def setPositionX(self, newPositionX):
        self.positionX = newPositionX

    def setPositionY(self, newPositionY):
        self.positionY = newPositionY

    # If true bounce right
    def setBounce(self, newBounce):
        self.bounceRight = newBounce


class EntityTennisBall(EntityGraphic):
    graphicPath = ""

class EntityVector:
    import Menus.GameMenuProperties as GameMenuProperties

    screenProperties = GameMenuProperties.GameMenuProperties()

    colorR = 255
    colorG = 255
    colorB = 230
    entityColor = (colorR, colorG, colorB)

    defaultSize = screenProperties.height / 25
    size = screenProperties.height / 25
    speed = screenProperties.width / 140
    defaultSpeed = screenProperties.width / 140
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

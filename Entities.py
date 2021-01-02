class EntityVector:
    colorR = 150
    colorG = 160
    colorB = 239
    entityColor = (colorR, colorG, colorB)

    speed = 3
    gravitySpeed = 0.4

    positionX = 100
    positionY = 100

    bounceRight = True

    def setSpeed(self, newSpeed):
        self.speed = newSpeed

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

    def setGravity(self, newGravity):
        self.gravitySpeed = newGravity

    # If true bounce right
    def setBounce(self, newBounce):
        self.bounceRight = newBounce


class EntityCircle(EntityVector):
    radius = 5

    def setRadius(self, newRadius):
        self.radius = newRadius


class EntitySquare(EntityVector):
    sideSize = 5

    def setSideSize(self, newSideSize):
        self.sideSize = newSideSize


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

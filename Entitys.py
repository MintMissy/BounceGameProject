class Entity:
    size = 20
    color = (255, 255, 255)
    speed = 3
    gravitySpeed = 50


class Circle(Entity):
    radius = 5


class Square(Entity):
    a = 5


class Graphic(Entity):
    graphicPath = ""


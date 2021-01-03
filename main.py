import pygame

import Entities
import ScreenProperties

pygame.init()

# Initiation of the window
pygame.display.set_caption("The name of window")
# TODO Setting an icon of program
# pygame.display.set_icon()
# Import screen properties class from file
screenProperties = ScreenProperties.ScreenProperties()
# Set screen size
screen = pygame.display.set_mode((screenProperties.width, screenProperties.height))

# Create entity at the middle of the screen
entity = Entities.EntityCircle()

# set size of entity
entity.setRadius(30)

# Make position of entity at the center of the screen
entity.setPositionX(screenProperties.getCenterX())
entity.setPositionY(screenProperties.getCenterY())

# set entity speed
entity.setSpeed(0.4)

# Setting gravity speed
entity.setGravity(0.5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.fill((screenProperties.getColor()))

    # entity = pygame.image.load('Zadanie2_ball.png')
    pygame.draw.circle(
        screen,
        entity.entityColor,
        (entity.positionX, entity.positionY),
        entity.radius)

    # Gravity
    if entity.positionY + entity.radius < screenProperties.height:
        entity.setPositionY(entity.positionY + entity.gravitySpeed)

    # Bouncing
    # If ball don't touch bottom continue
    if entity.positionY < screenProperties.height - entity.radius:
        if entity.bounceRight:
            # If ball touch right side change bounce direction
            if entity.positionX + entity.radius >= screenProperties.width:
                entity.setBounce(False)
            # Move ball it to right
            entity.setPositionX(entity.positionX + entity.speed)

        else:
            # If ball touch left side change bounce direction
            if entity.positionX <= 0 + entity.radius:
                entity.setBounce(True)
            # Move ball it to left
            entity.setPositionX(entity.positionX - entity.speed)

    pygame.display.flip()

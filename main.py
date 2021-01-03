import pygame

import TextProperties
import Entities
import ScreenProperties

pygame.init()

# Initiation of the window
pygame.display.set_caption("My game in Py game")
# Setting an icon of program
programIcon = pygame.image.load('Graphics/ProgramIcon.png')
pygame.display.set_icon(programIcon)
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
entity.setGravity(0.2)

# Setting score value
score = 0
# Setting basic font options
textProperties = TextProperties.Text()

font = pygame.font.Font(textProperties.font, textProperties.size)
text = font.render(str(score), True, textProperties.textColor)
text_rect = text.get_rect(center=
                          (screenProperties.getCenterX(),
                           screenProperties.getCenterY() - screenProperties.width / 7))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # Check if player use space to jump ball
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                entity.setGravity(-0.6)

    # Gravity
    if entity.positionY + entity.radius < screenProperties.height:
        entity.setPositionY(entity.positionY + entity.gravitySpeed)
        entity.setGravity(entity.gravitySpeed + 0.0015)

    # Bouncing
    # If ball don't touch bottom continue
    if entity.positionY < screenProperties.height - entity.radius:
        # If ball touch top place it under and set default gravity
        if not entity.positionY - entity.radius > 0:
            entity.setPositionY(1 + entity.radius)
            entity.setGravity(0.05)
        # If ball don't touch top continue
        else:
            if entity.bounceRight:
                # If ball touch right side change bounce direction
                if entity.positionX + entity.radius >= screenProperties.width:
                    entity.setBounce(False)
                    score += 1
                # Move ball it to right
                entity.setPositionX(entity.positionX + entity.speed)
            else:
                # If ball touch left side change bounce direction
                if entity.positionX <= 0 + entity.radius:
                    entity.setBounce(True)
                    score += 1
                # Move ball it to left
                entity.setPositionX(entity.positionX - entity.speed)

    screen.fill((screenProperties.getColor()))

    # If score is 10/100/1000 center it
    if score == 10 or 100 or 1000:
        text_rect = text.get_rect(center=
                                  (screenProperties.getCenterX(),
                                   screenProperties.getCenterY() - screenProperties.width / 7))
    # Draw score at screen
    text = font.render(str(score), True, textProperties.textColor)
    screen.blit(text, text_rect)

    # Draw an object
    pygame.draw.circle(
        screen,
        entity.entityColor,
        (entity.positionX, entity.positionY),
        entity.radius)

    pygame.display.flip()

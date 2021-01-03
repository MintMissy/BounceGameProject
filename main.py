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

# Setting score value
score = 0

# Setting basic font options
scoreProperties = TextProperties.Text()
# Create new text that show score
fontScore = pygame.font.Font(scoreProperties.font, scoreProperties.size)
textScore = fontScore.render(str(score), True, scoreProperties.textColor)
textScore_rect = textScore.get_rect(center=
                          (screenProperties.getCenterX(),
                           screenProperties.getCenterY() - screenProperties.width / 7))
# Create new text that is visible if player lose
gameOverProperties = TextProperties.Text()
gameOverProperties.setSize(70)
fontGameOver = pygame.font.Font(gameOverProperties.font, gameOverProperties.size)
textGameOver = fontGameOver.render("Game Over", True, gameOverProperties.textColor)
textGameOver_rect = textGameOver.get_rect(center=
                          (screenProperties.getCenterX(),
                           screenProperties.getCenterY() - screenProperties.width / 5))

# Variable that checks if player lost
gameOver = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # Check if player use space to jump ball
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                entity.setGravity(entity.defaultJumpHeight)

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
    else:
        gameOver = True

    screen.fill((screenProperties.getColor()))

    # Score text appears when game is on
    if not gameOver:
        # If score is 10/100/1000 center it
        if score == 10 or 100 or 1000:
            textScore_rect = textScore.get_rect(center=
                                      (screenProperties.getCenterX(),
                                       screenProperties.getCenterY() - screenProperties.width / 7))
        # Draw score at screen
        textScore = fontScore.render(str(score), True, scoreProperties.textColor)
        screen.blit(textScore, textScore_rect)

    # What happens if game is off
    if gameOver:
        # Game over title
        screen.blit(textGameOver, textGameOver_rect)
        # Refresh your score title
        textScore_rect = textScore.get_rect(center=
                                            (screenProperties.getCenterX(),
                                             screenProperties.getCenterY() - screenProperties.width / 10))
        scoreProperties.setSize(40)
        fontScore = pygame.font.Font(scoreProperties.font, scoreProperties.size)
        textScore = fontScore.render("Your score " + str(score), True, scoreProperties.textColor)
        screen.blit(textScore, textScore_rect)

    # Draw an object (ball etc)
    pygame.draw.circle(
        screen,
        entity.entityColor,
        (entity.positionX, entity.positionY),
        entity.radius)

    pygame.display.flip()

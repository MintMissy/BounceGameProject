import pygame

import TextProperties
import EntitiesProperties
import ScreenProperties
import SpikesProperties

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
entityProperties = EntitiesProperties.EntityCircle()

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

# Create instance of left spikes properties
spikePropertiesL = SpikesProperties.LeftSpike()
spikePropertiesL.refreshPositionY()
# Create instance of right spikes properties
spikePropertiesR = SpikesProperties.RightSpike()

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
                entityProperties.setGravity(entityProperties.defaultJumpHeight)
            if event.key == pygame.K_BACKSPACE:
                gameOver = False
                entityProperties.setPositionY(screenProperties.height / 2)
                entityProperties.setPositionX(screenProperties.width / 2)
                entityProperties.setRadius(30)
                entityProperties.setSpeed(entityProperties.defaultSpeed)
                entityProperties.setGravity(entityProperties.defaultGravity)

    # Gravity
    if entityProperties.positionY + entityProperties.radius < screenProperties.height:
        entityProperties.setPositionY(entityProperties.positionY + entityProperties.gravitySpeed)
        entityProperties.setGravity(entityProperties.gravitySpeed + 0.0015)

    # Bouncing
    # If ball don't touch bottom continue
    if entityProperties.positionY < screenProperties.height - entityProperties.radius:
        # If ball touch top place it under and set default gravity
        if not entityProperties.positionY - entityProperties.radius > 0:
            entityProperties.setPositionY(1 + entityProperties.radius)
            entityProperties.setGravity(0.05)
        # If ball don't touch top continue
        else:
            if entityProperties.bounceRight:
                # If ball touch right side change bounce direction
                if entityProperties.positionX + entityProperties.radius >= screenProperties.width:
                    entityProperties.setBounce(False)
                    score += 1
                    # Change position of left spike
                    spikePropertiesL.refreshPositionY()
                # Move ball it to right
                entityProperties.setPositionX(entityProperties.positionX + entityProperties.speed)
            else:
                # If ball touch left side change bounce direction
                if entityProperties.positionX <= 0 + entityProperties.radius:
                    entityProperties.setBounce(True)
                    score += 1
                    # Change position of right spike
                    spikePropertiesR.refreshPositionY()
                # Move ball it to left
                entityProperties.setPositionX(entityProperties.positionX - entityProperties.speed)
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
        # Smoothly change size of entity to 0 if it died
        if entityProperties.radius > 0:
            entityProperties.setRadius(entityProperties.radius - 0.2)
            entityProperties.setSpeed(0)

    # Draw an object (ball etc)
    entity = pygame.draw.circle(
        screen,
        entityProperties.entityColor,
        (entityProperties.positionX, entityProperties.positionY),
        entityProperties.radius)

    # Create spikes on the screen
    spikeRight = spikePropertiesR.createSpike(screen)
    spikeLeft = spikePropertiesL.createSpike(screen)

    # Spikes visible Collision with spike
    if entity.colliderect(spikeRight or spikeLeft):
        gameOver = True

    pygame.display.flip()

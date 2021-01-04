import pygame

import TextProperties
import EntitiesProperties
from Menus import GameMenuProperties
import SpikesProperties
from Menus import StartMenuProperties

pygame.init()

# Initiation of the window
pygame.display.set_caption("My game in Py game")
# Setting an icon of program
programIcon = pygame.image.load('Graphics/ProgramIcon.png')
pygame.display.set_icon(programIcon)

# GAME MENU OPTIONS
# Import game screen properties class from file
gameMenuProperties = GameMenuProperties.GameMenuProperties()
# Set game screen size
gameScreen = pygame.display.set_mode((gameMenuProperties.width, gameMenuProperties.height))
# Variable that checks if player lost
gameOver = False
# Create instance of left spikes properties
spikePropertiesL = SpikesProperties.LeftSpike()
spikePropertiesL.refreshPositionY()
# Create instance of right spikes properties
spikePropertiesR = SpikesProperties.RightSpike()
# Create entity at the middle of the screen
entityProperties = EntitiesProperties.EntityCircle()

# START MENU PROPERTIES
# Import start screen properties class from file
startMenuProperties = StartMenuProperties.StartMenuProperties()
# Set game screen size
startScreen = pygame.display.set_mode((startMenuProperties.width, startMenuProperties.height))

# GAME OVER MENU
# Setting score value
score = 0
# Setting basic font options
scoreProperties = TextProperties.Text()
# Create new text that show score
fontScore = pygame.font.Font(scoreProperties.font, scoreProperties.size)
textScore = fontScore.render(str(score), True, scoreProperties.textColor)
textScore_rect = textScore.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() - gameMenuProperties.width / 7))
# Create new text that is visible if player lose
gameOverProperties = TextProperties.Text()
gameOverProperties.setSize(70)
fontGameOver = pygame.font.Font(gameOverProperties.font, gameOverProperties.size)
textGameOver = fontGameOver.render("Game Over", True, gameOverProperties.textColor)
textGameOver_rect = textGameOver.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() - gameMenuProperties.width / 5))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # Check if player use space to jump ball
        if event.type == pygame.KEYDOWN:
            # Checking keyboard and mouse in game
            if startMenuProperties.gameStart:
                if event.key == pygame.K_SPACE:
                    entityProperties.setGravity(entityProperties.defaultJumpHeight)
            # Checking keyboard and mouse in start menu
            else:
                if event.key == pygame.K_BACKSPACE:
                    startMenuProperties.setGameStart(True)
                # gameOver = False
                # entityProperties.setPositionY(screenProperties.height / 2)
                # entityProperties.setPositionX(screenProperties.width / 2)
                # entityProperties.setRadius(30)
                # entityProperties.setSpeed(entityProperties.defaultSpeed)
                # entityProperties.setGravity(entityProperties.defaultGravity)
                # score = 0

    # PLAYER IN MAIN MENU
    if not startMenuProperties.gameStart:
        # Clear every frame
        gameScreen.fill((startMenuProperties.getColor()))




    # PLAYER IN GAME
    else:
        # Clear every frame
        gameScreen.fill((gameMenuProperties.getColor()))

        # SHOW SCORE AT SCREEN
        # SHOW SCORE AT SCREEN
        if not gameOver:
            # If score is 10/100/1000 center it
            if score == 10 or 100 or 1000:
                textScore_rect = textScore.get_rect(
                    center=(
                        gameMenuProperties.getCenterX(),
                        gameMenuProperties.getCenterY() - gameMenuProperties.width / 7))
            # Draw score at screen
            textScore = fontScore.render(str(score), True, scoreProperties.textColor)
            gameScreen.blit(textScore, textScore_rect)

        # GAME OVER
        if gameOver:
            # Game over title
            gameScreen.blit(textGameOver, textGameOver_rect)
            # Refresh your score title
            textScore_rect = textScore.get_rect(
                center=(
                    gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() - gameMenuProperties.width / 10))
            scoreProperties.setSize(40)
            fontScore = pygame.font.Font(scoreProperties.font, scoreProperties.size)
            textScore = fontScore.render("Your score " + str(score), True, scoreProperties.textColor)
            gameScreen.blit(textScore, textScore_rect)
            # Smoothly change size of entity to 0 if it died
            if entityProperties.radius > 0:
                entityProperties.setRadius(entityProperties.radius - 0.2)
                entityProperties.setSpeed(0)

        # DRAW ENTITY
        entity = pygame.draw.circle(
            gameScreen,
            entityProperties.entityColor,
            (entityProperties.positionX, entityProperties.positionY),
            entityProperties.radius)

        # Create spikes on the screen
        spikeRight = spikePropertiesR.createSpike(gameScreen)
        spikeLeft = spikePropertiesL.createSpike(gameScreen)

        # PHYSICS
        # Gravity
        if entityProperties.positionY + entityProperties.radius < gameMenuProperties.height:
            entityProperties.setPositionY(entityProperties.positionY + entityProperties.gravitySpeed)
            entityProperties.setGravity(entityProperties.gravitySpeed + 0.0015)

        # Bouncing
        # If ball don't touch bottom continue
        if entityProperties.positionY < gameMenuProperties.height - entityProperties.radius:
            # If ball touch top place it under and set default gravity
            if not entityProperties.positionY - entityProperties.radius > 0:
                entityProperties.setPositionY(1 + entityProperties.radius)
                entityProperties.setGravity(0.05)
            # If ball don't touch top continue
            else:
                if entityProperties.bounceRight:
                    # If ball touch right side change bounce direction
                    if entityProperties.positionX + entityProperties.radius >= gameMenuProperties.width:
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

        # Spikes visible Collision with spike
        if entity.colliderect(spikeRight):
            gameOver = True
        elif entity.colliderect(spikeLeft):
            gameOver = True

    pygame.display.flip()

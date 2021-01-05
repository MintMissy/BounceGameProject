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


# Method that creates text
def createText(properties, size, colors, title):
    properties.setSize(size)
    properties.setColors(colors[0], colors[1], colors[2])
    properties.refreshColor()
    font = pygame.font.Font(properties.font, properties.size)
    text = font.render(title, True, properties.textColor)
    return text


# START MENU PROPERTIES
# Import start screen properties class from file
startMenuProperties = StartMenuProperties.StartMenuProperties()
# Set game screen size
startScreen = pygame.display.set_mode((startMenuProperties.width, startMenuProperties.height))
# Bounce Game Title
bounceGameProperties = TextProperties.Text()
textBounceGame = createText(bounceGameProperties, 70, bounceGameProperties.textColor, "Bounce Game")
textBounceGame_rect = textBounceGame.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8))

# Start Game Title
startGameProperties = TextProperties.Text()
textStartGame = createText(startGameProperties, 50, (240, 240, 90), "Start")
textStartGame_rect = textStartGame.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 3))

# Options Title
optionsProperties = TextProperties.Text()
textOptions = createText(optionsProperties, 50, (240, 240, 90), "Options")
textOptions_rect = textOptions.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 4))

# Credits Title
creditsProperties = TextProperties.Text()
textCredits = createText(creditsProperties, 50, (240, 240, 90), "Credits")
textCredits_rect = textCredits.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 5))

# Quit Title
quitProperties = TextProperties.Text()
textQuit = createText(quitProperties, 50, (240, 240, 90), "Quit")
textQuit_rect = textQuit.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 6))

# GAME OVER MENU
# Setting score value
score = 0
# Create new text that show score in the game
scoreProperties = TextProperties.Text()
textScore = createText(scoreProperties, scoreProperties.size, scoreProperties.textColor, str(score))
textScore_rect = textScore.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() - gameMenuProperties.width / 7))

# Create new text GAME OVER that is visible if player lose
gameOverProperties = TextProperties.Text()
textGameOver = createText(gameOverProperties, 70, gameOverProperties.textColor, "Game Over")
textGameOver_rect = textGameOver.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() - gameMenuProperties.width / 5))

# Create new text Play Again that is visible if player lose
playAgainProperties = TextProperties.Text()
textPlayAgain = createText(playAgainProperties, 40, (240, 240, 90), "Play Again")
textPlayAgain_rect = textPlayAgain.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() + gameMenuProperties.width / 40))

# Create new text Options that is visible if player lose
optionsOverProperties = TextProperties.Text()
textOptionsOver = createText(optionsOverProperties, 40, (240, 240, 90), "Options")
textOptionsOver_rect = textOptionsOver.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() + gameMenuProperties.width / 40 * 4))

# Create new text Back to lobby that is visible if player lose
backLobbyProperties = TextProperties.Text()
textBackLobby = createText(backLobbyProperties, 40, (240, 240, 90), "Back to Lobby")
textBackLobby_rect = textBackLobby.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() + gameMenuProperties.width / 40 * 7))

skin = "Circle"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # BALL JUMP OPTIONS
        # Check if player use space to jump ball
        if event.type == pygame.KEYDOWN:
            # Checking keyboard and mouse in game
            if startMenuProperties.gameStart and not gameOver:
                if event.key == pygame.K_SPACE:
                    entityProperties.setGravity(entityProperties.defaultJumpHeight)
        # Check if player use LMB to jump ball
        if event.type == pygame.MOUSEBUTTONUP:
            if startMenuProperties.gameStart and not gameOver:
                entityProperties.setGravity(entityProperties.defaultJumpHeight)

        # BUTTON GLOW
        # If mouse collides with button it glows

        # Get Mouse potion
        mousePosition = pygame.mouse.get_pos()

        # REFRESH START MAIN MENU
        if not startMenuProperties.gameStart:
            # Check if player hover Start Game button if do, change color of button
            if textStartGame_rect.collidepoint(mousePosition):
                textStartGame = createText(startGameProperties, startGameProperties.size, (240, 240, 150), "Start")
                # Check if player clicked Start Game button Start if it do start game
                if event.type == pygame.MOUSEBUTTONUP:
                    startMenuProperties.setGameStart(True)
            # If player didn't hover Start Game change it color to normal
            else:
                textStartGame = createText(startGameProperties, startGameProperties.size, (240, 240, 90), "Start")

            # Check if player hover Options button if do, change color of button
            if textOptions_rect.collidepoint(mousePosition):
                textOptions = createText(optionsProperties, optionsProperties.size, (240, 240, 150), "Options")
                # Check if player clicked Options button Start if it do move to options menu
                if event.type == pygame.MOUSEBUTTONUP:
                    # TODO add options menu with skins
                    print("I should add options")
            # If player didn't hover Options button change it color to normal
            else:
                textOptions = createText(optionsProperties, optionsProperties.size, (240, 240, 90), "Options")

            # Check if player hover Credits button if do, change color of button
            if textCredits_rect.collidepoint(mousePosition):
                textCredits = createText(creditsProperties, creditsProperties.size, (240, 240, 150), "Credits")
                # Check if player clicked Credits button Start if it do move to Credits menu
                if event.type == pygame.MOUSEBUTTONUP:
                    # TODO add credits menu with my name
                    print("I should add credits")
            # If player didn't hover Credits button change it color to normal
            else:
                textCredits = createText(creditsProperties, creditsProperties.size, (240, 240, 90), "Credits")

            # Check if player hover Quit button if do, change color of button
            if textQuit_rect.collidepoint(mousePosition):
                textQuit = createText(quitProperties, quitProperties.size, (240, 240, 150), "Quit")
                # Check if player clicked Quit button if it do close game
                if event.type == pygame.MOUSEBUTTONUP:
                    exit(0)
            # If player didn't hover Quit button change it color to normal
            else:
                textQuit = createText(quitProperties, quitProperties.size, (240, 240, 90), "Quit")

        # REFRESH GAME OVER BUTTONS
        else:
            # CHECK BUTTONS AFTER PLAYER LOST
            if gameOver:
                # Check if player hover Play Again button if do, change color of button
                if textPlayAgain_rect.collidepoint(mousePosition):
                    textPlayAgain = createText(playAgainProperties, playAgainProperties.size, (240, 240, 150),
                                               "Play Again")
                    # Check if player clicked PLAY AGAIN button if it do move to Play again menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        score = 0
                        gameOver = False
                        # Reset spikes position
                        spikePropertiesL = SpikesProperties.LeftSpike()
                        spikePropertiesL.refreshPositionY()
                        spikePropertiesR = SpikesProperties.RightSpike()
                        # Reset entity position
                        entityProperties = EntitiesProperties.EntityCircle()
                        entityProperties.setPositionY(gameMenuProperties.height / 2)
                        entityProperties.setPositionX(gameMenuProperties.width / 2)
                        entityProperties.setSize(entityProperties.defaultSize)
                        entityProperties.setSpeed(entityProperties.defaultSpeed)
                        entityProperties.setGravity(entityProperties.defaultGravity)
                        # Reset score title position
                        textScore = createText(scoreProperties, 100, (58, 58, 64), str(score))
                # If player didn't hover PLAY AGAIN button change it color to normal
                else:
                    textPlayAgain = createText(playAgainProperties, playAgainProperties.size, (240, 240, 90),
                                               "Play Again")
                    playAgainProperties.setColors(240, 240, 90)

                # Check if player hover Options button if do, change color of button
                if textOptionsOver_rect.collidepoint(mousePosition):
                    textOptionsOver = createText(optionsOverProperties, optionsOverProperties.size, (240, 240, 150),
                                                 "Options")
                    # Check if player clicked PLAY AGAIN button if it do move to OPTIONS menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        # TODO add options menu with skins
                        print("I should add options")
                # If player didn't hover OPTIONS button change it color to normal
                else:
                    textOptionsOver = createText(optionsOverProperties, optionsOverProperties.size, (240, 240, 90),
                                                 "Options")

                # Check if player hover BACK TO LOBBY button if do, change color of button
                if textBackLobby_rect.collidepoint(mousePosition):
                    textBackLobby = createText(backLobbyProperties, backLobbyProperties.size, (240, 240, 150),
                                               "Back to Lobby")
                    # Check if player clicked BACK TO LOBBY button if it do move to Main Menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        # TODO add exit to main menu
                        print("I should add back to main menu")
                # If player didn't hover BACK TO LOBBY button change it color to normal
                else:
                    textBackLobby = createText(backLobbyProperties, backLobbyProperties.size, (240, 240, 90),
                                               "Back to Lobby")

    # PLAYER IN MAIN MENU
    if not startMenuProperties.gameStart:
        # Clear every frame
        gameScreen.fill(startMenuProperties.screenColor)

        # Bounce Game title
        gameScreen.blit(textBounceGame, textBounceGame_rect)
        gameScreen.blit(textStartGame, textStartGame_rect)
        gameScreen.blit(textOptions, textOptions_rect)
        gameScreen.blit(textCredits, textCredits_rect)
        gameScreen.blit(textQuit, textQuit_rect)
        # Create first button
        # startButton = pygame.draw.rect(
        #     startScreen,
        #     startMenuProperties.buttonColor,
        #     ([startMenuProperties.width / 4, startMenuProperties.height / 6],
        #      [startMenuProperties.width / 4 * 2, startMenuProperties.height / 6 * 1.0005])
        #
        # )


    # PLAYER IN GAME
    else:
        # Clear every frame
        gameScreen.fill(gameMenuProperties.screenColor)

        # SHOW SCORE AT SCREEN
        # SHOW SCORE AT SCREEN
        if not gameOver:
            # If score is 10/100/1000 center it
            if score == 10 or 100 or 1000:
                textScore_rect = textScore.get_rect(
                    center=(
                        gameMenuProperties.getCenterX(),
                        gameMenuProperties.getCenterY() - gameMenuProperties.width / 7))
            # Change color of score title in game
            textScore = createText(scoreProperties, scoreProperties.size, (58, 58, 64), str(score))
            # Draw score at screen
            gameScreen.blit(textScore, textScore_rect)

        # GAME OVER
        if gameOver:
            # Game over title
            gameScreen.blit(textGameOver, textGameOver_rect)
            gameScreen.blit(textPlayAgain, textPlayAgain_rect)
            gameScreen.blit(textOptionsOver, textOptionsOver_rect)
            gameScreen.blit(textBackLobby, textBackLobby_rect)

            # Refresh your score title
            textScore_rect = textScore.get_rect(
                center=(
                    gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() - gameMenuProperties.width / 10))
            textScore = createText(scoreProperties, 40, (255, 255, 64), ("Your score " + str(score)))
            # Draw your score title at game over screen
            gameScreen.blit(textScore, textScore_rect)
            # Smoothly change size of entity to 0 if it died
            if entityProperties.size > 0:
                entityProperties.setSize(entityProperties.size - 0.2)
                entityProperties.setSpeed(0)

        skin = "TriangleBorder"
        # DRAW ENTITY WITH SKIN
        if skin == "CircleBorder":
            entity = pygame.draw.circle(
                gameScreen,
                entityProperties.entityColor,
                (entityProperties.positionX, entityProperties.positionY),
                entityProperties.size,
                10)
        elif skin == "Circle":
            entity = pygame.draw.circle(
                gameScreen,
                entityProperties.entityColor,
                (entityProperties.positionX, entityProperties.positionY),
                entityProperties.size)
        elif skin == "Square":
            entity = pygame.draw.rect(
                gameScreen,
                entityProperties.entityColor,
                [entityProperties.positionX - entityProperties.size,
                 entityProperties.positionY - entityProperties.size,
                 entityProperties.size * 2,
                 entityProperties.size * 2
                 ]
            )
        elif skin == "SquareBorder":
            entity = pygame.draw.rect(
                gameScreen,
                entityProperties.entityColor,
                [entityProperties.positionX - entityProperties.size,
                 entityProperties.positionY - entityProperties.size,
                 entityProperties.size * 2,
                 entityProperties.size * 2
                 ],
                10
            )
        elif skin == "Triangle":
            entity = pygame.draw.polygon(
                gameScreen,
                entityProperties.entityColor,
                [(entityProperties.positionX, entityProperties.positionY + entityProperties.size),
                (entityProperties.positionX - entityProperties.size, entityProperties.positionY - entityProperties.size),
                (entityProperties.positionX + entityProperties.size, entityProperties.positionY - entityProperties.size)]
            )
        elif skin == "TriangleBorder":
            entity = pygame.draw.polygon(
                gameScreen,
                entityProperties.entityColor,
                [(entityProperties.positionX, entityProperties.positionY + entityProperties.size),
                (entityProperties.positionX - entityProperties.size, entityProperties.positionY - entityProperties.size),
                (entityProperties.positionX + entityProperties.size, entityProperties.positionY - entityProperties.size)],
                10
            )


        # Create spikes on the screen
        spikeRight = spikePropertiesR.createSpike(gameScreen)
        spikeLeft = spikePropertiesL.createSpike(gameScreen)

        # PHYSICS
        # Gravity
        if entityProperties.positionY + entityProperties.size < gameMenuProperties.height:
            entityProperties.setPositionY(entityProperties.positionY + entityProperties.gravitySpeed)
            entityProperties.setGravity(entityProperties.gravitySpeed + 0.0015)

        # Bouncing
        # If ball don't touch bottom continue
        if entityProperties.positionY < gameMenuProperties.height - entityProperties.size:
            # If ball touch top place it under and set default gravity
            if not entityProperties.positionY - entityProperties.size > 0:
                entityProperties.setPositionY(1 + entityProperties.size)
                entityProperties.setGravity(0.05)
            # If ball don't touch top continue
            else:
                if entityProperties.bounceRight:
                    # If ball touch right side change bounce direction
                    if entityProperties.positionX + entityProperties.size >= gameMenuProperties.width:
                        entityProperties.setBounce(False)
                        score += 1
                        # Change position of left spike
                        spikePropertiesL.refreshPositionY()
                    # Move ball it to right
                    entityProperties.setPositionX(entityProperties.positionX + entityProperties.speed)
                else:
                    # If ball touch left side change bounce direction
                    if entityProperties.positionX <= 0 + entityProperties.size:
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

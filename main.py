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
# Bounce Game Title
bounceGameProperties = TextProperties.Text()
bounceGameProperties.setSize(70)
fontBounceGame = pygame.font.Font(bounceGameProperties.font, bounceGameProperties.size)
textBounceGame = fontBounceGame.render("Bounce Game", True, bounceGameProperties.textColor)
textBounceGame_rect = textBounceGame.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8))
# Start Game Title
startGameProperties = TextProperties.Text()
startGameProperties.setSize(50)
startGameProperties.setColors(240, 240, 90)
startGameProperties.refreshColor()
fontStartGame = pygame.font.Font(startGameProperties.font, startGameProperties.size)
textStartGame = fontStartGame.render("Start", True, startGameProperties.textColor)
textStartGame_rect = textStartGame.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 3))
# Options Title
optionsProperties = TextProperties.Text()
optionsProperties.setSize(50)
optionsProperties.setColors(240, 240, 90)
optionsProperties.refreshColor()
fontOptions = pygame.font.Font(optionsProperties.font, optionsProperties.size)
textOptions = fontOptions.render("Options", True, optionsProperties.textColor)
textOptions_rect = textOptions.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 4))
# Credits Title
creditsProperties = TextProperties.Text()
creditsProperties.setSize(50)
creditsProperties.setColors(240, 240, 90)
creditsProperties.refreshColor()
creditsOptions = pygame.font.Font(creditsProperties.font, creditsProperties.size)
textCredits = creditsOptions.render("Credits", True, creditsProperties.textColor)
textCredits_rect = textCredits.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 5))
# Quit Title
quitProperties = TextProperties.Text()
quitProperties.setSize(50)
quitProperties.setColors(240, 240, 90)
quitProperties.refreshColor()
fontQuit = pygame.font.Font(quitProperties.font, quitProperties.size)
textQuit = fontQuit.render("Quit", True, quitProperties.textColor)
textQuit_rect = textQuit.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 6))

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
# Create new text GAME OVER that is visible if player lose
gameOverProperties = TextProperties.Text()
gameOverProperties.setSize(70)
fontGameOver = pygame.font.Font(gameOverProperties.font, gameOverProperties.size)
textGameOver = fontGameOver.render("Game Over", True, gameOverProperties.textColor)
textGameOver_rect = textGameOver.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() - gameMenuProperties.width / 5))
# Create new text Play Again that is visible if player lose
playAgainProperties = TextProperties.Text()
playAgainProperties.setSize(40)
playAgainProperties.setColors(240, 240, 90)
playAgainProperties.refreshColor()
fontPlayAgain = pygame.font.Font(playAgainProperties.font, playAgainProperties.size)
textPlayAgain = fontPlayAgain.render("Play Again", True, playAgainProperties.textColor)
textPlayAgain_rect = textPlayAgain.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() + gameMenuProperties.width / 40))
# Create new text Play Again that is visible if player lose
optionsOverProperties = TextProperties.Text()
optionsOverProperties.setSize(40)
optionsOverProperties.setColors(240, 240, 90)
optionsOverProperties.refreshColor()
fontOptionsOver = pygame.font.Font(optionsOverProperties.font, optionsOverProperties.size)
textOptionsOver = fontOptionsOver.render("Options", True, optionsOverProperties.textColor)
textOptionsOver_rect = textOptionsOver.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() + gameMenuProperties.width / 40 * 4))
# Create new text Play Again that is visible if player lose
backLobbyProperties = TextProperties.Text()
backLobbyProperties.setSize(40)
backLobbyProperties.setColors(240, 240, 90)
backLobbyProperties.refreshColor()
fontBackLobby = pygame.font.Font(backLobbyProperties.font, backLobbyProperties.size)
textBackLobby = fontBackLobby.render("Back to Lobby", True, backLobbyProperties.textColor)
textBackLobby_rect = textBackLobby.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() + gameMenuProperties.width / 40 * 7))

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
                startGameProperties.setColors(240, 240, 150)
                startGameProperties.refreshColor()
                fontStartGame = pygame.font.Font(startGameProperties.font, startGameProperties.size)
                textStartGame = fontStartGame.render("Start", True, startGameProperties.textColor)
                # Check if player clicked Start Game button Start if it do start game
                if event.type == pygame.MOUSEBUTTONUP:
                    startMenuProperties.setGameStart(True)
            # If player didn't hover Start Game change it color to normal
            else:
                startGameProperties.setColors(240, 240, 90)
                startGameProperties.refreshColor()
                fontStartGame = pygame.font.Font(startGameProperties.font, startGameProperties.size)
                textStartGame = fontStartGame.render("Start", True, startGameProperties.textColor)

            # Check if player hover Options button if do, change color of button
            if textOptions_rect.collidepoint(mousePosition):
                optionsProperties.setColors(240, 240, 150)
                optionsProperties.refreshColor()
                fontOptions = pygame.font.Font(optionsProperties.font, optionsProperties.size)
                textOptions = fontOptions.render("Options", True, optionsProperties.textColor)
                # Check if player clicked Options button Start if it do move to options menu
                if event.type == pygame.MOUSEBUTTONUP:
                    # TODO add options menu with skins
                    print("I should add options")
            # If player didn't hover Options button change it color to normal
            else:
                optionsProperties.setColors(240, 240, 90)
                optionsProperties.refreshColor()
                fontOptions = pygame.font.Font(optionsProperties.font, optionsProperties.size)
                textOptions = fontOptions.render("Options", True, optionsProperties.textColor)

            # Check if player hover Credits button if do, change color of button
            if textCredits_rect.collidepoint(mousePosition):
                creditsProperties.setColors(240, 240, 150)
                creditsProperties.refreshColor()
                creditsOptions = pygame.font.Font(creditsProperties.font, creditsProperties.size)
                textCredits = creditsOptions.render("Credits", True, creditsProperties.textColor)
                # Check if player clicked Credits button Start if it do move to Credits menu
                if event.type == pygame.MOUSEBUTTONUP:
                    # TODO add credits menu with my name
                    print("I should add credits")
            # If player didn't hover Credits button change it color to normal
            else:
                creditsProperties.setColors(240, 240, 90)
                creditsProperties.refreshColor()
                creditsOptions = pygame.font.Font(creditsProperties.font, creditsProperties.size)
                textCredits = creditsOptions.render("Credits", True, creditsProperties.textColor)

            # Check if player hover Quit button if do, change color of button
            if textQuit_rect.collidepoint(mousePosition):
                quitProperties.setColors(240, 240, 150)
                quitProperties.refreshColor()
                fontQuit = pygame.font.Font(quitProperties.font, quitProperties.size)
                textQuit = fontQuit.render("Quit", True, quitProperties.textColor)
                # Check if player clicked Quit button if it do close game
                if event.type == pygame.MOUSEBUTTONUP:
                    exit(0)
            # If player didn't hover Quit button change it color to normal
            else:
                quitProperties.setColors(240, 240, 90)
                quitProperties.refreshColor()
                fontQuit = pygame.font.Font(quitProperties.font, quitProperties.size)
                textQuit = fontQuit.render("Quit", True, quitProperties.textColor)

        # REFRESH GAME OVER BUTTONS
        else:
            # CHECK BUTTONS AFTER PLAYER LOST
            if gameOver:
                # Check if player hover Play Again button if do, change color of button
                if textPlayAgain_rect.collidepoint(mousePosition):
                    playAgainProperties.setColors(240, 240, 150)
                    playAgainProperties.refreshColor()
                    fontPlayAgain = pygame.font.Font(playAgainProperties.font, playAgainProperties.size)
                    textPlayAgain = fontPlayAgain.render("Play Again", True, playAgainProperties.textColor)
                    # Check if player clicked PLAY AGAIN button if it do move to Play again menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        # TODO add play again option
                        # gameOver = False
                        # entityProperties.setPositionY(screenProperties.height / 2)
                        # entityProperties.setPositionX(screenProperties.width / 2)
                        # entityProperties.setRadius(30)
                        # entityProperties.setSpeed(entityProperties.defaultSpeed)
                        # entityProperties.setGravity(entityProperties.defaultGravity)
                        # score = 0
                        print("I should add play again")
                # If player didn't hover PLAY AGAIN button change it color to normal
                else:
                    playAgainProperties.setColors(240, 240, 90)
                    playAgainProperties.refreshColor()
                    fontPlayAgain = pygame.font.Font(playAgainProperties.font, playAgainProperties.size)
                    textPlayAgain = fontPlayAgain.render("Play Again", True, playAgainProperties.textColor)

                # Check if player hover Options button if do, change color of button
                if textOptionsOver_rect.collidepoint(mousePosition):
                    optionsOverProperties.setColors(240, 240, 150)
                    optionsOverProperties.refreshColor()
                    fontOptionsOver = pygame.font.Font(optionsOverProperties.font, optionsOverProperties.size)
                    textOptionsOver = fontOptionsOver.render("Options", True, optionsOverProperties.textColor)
                    # Check if player clicked PLAY AGAIN button if it do move to OPTIONS menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        # TODO add options menu with skins
                        print("I should add options")
                # If player didn't hover OPTIONS button change it color to normal
                else:
                    optionsOverProperties.setColors(240, 240, 90)
                    optionsOverProperties.refreshColor()
                    fontOptionsOver = pygame.font.Font(optionsOverProperties.font, optionsOverProperties.size)
                    textOptionsOver = fontOptionsOver.render("Options", True, optionsOverProperties.textColor)

                # Check if player hover BACK TO LOBBY button if do, change color of button
                if textBackLobby_rect.collidepoint(mousePosition):
                    backLobbyProperties.setColors(240, 240, 150)
                    backLobbyProperties.refreshColor()
                    fontBackLobby = pygame.font.Font(backLobbyProperties.font, backLobbyProperties.size)
                    textBackLobby = fontBackLobby.render("Back to Lobby", True, backLobbyProperties.textColor)
                    # Check if player clicked BACK TO LOBBY button if it do move to Main Menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        # TODO add exit to main menu
                        print("I should add back to main menu")
                # If player didn't hover BACK TO LOBBY button change it color to normal
                else:
                    backLobbyProperties.setColors(240, 240, 90)
                    backLobbyProperties.refreshColor()
                    fontBackLobby = pygame.font.Font(backLobbyProperties.font, backLobbyProperties.size)
                    textBackLobby = fontBackLobby.render("Back to Lobby", True, backLobbyProperties.textColor)

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
            scoreProperties.setColors(58, 58, 64)
            scoreProperties.refreshColor()
            # Draw score at screen
            textScore = fontScore.render(str(score), True, scoreProperties.textColor)
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
            scoreProperties.setSize(40)
            # Change color of score title to yellow
            scoreProperties.setColors(255, 255, 64)
            scoreProperties.refreshColor()
            # Draw your score title at game over screen
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

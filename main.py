import pygame

import random
import TextProperties
import EntitiesProperties
from Menus import GameMenuProperties
import SpikesProperties
from Menus import StartMenuProperties

pygame.init()

# Initiation of the window
pygame.display.set_caption("<> Bounce Game <>")
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

# Create instances of left spikes properties
leftSpikesProperties = []
# Add 16 spikes to list
for i in range(16):
    leftSpikesProperties.append(SpikesProperties.LeftSpike())
    leftSpikesProperties[i - 1].setPositionY((i - 1) * (gameMenuProperties.height / 15))

# Create instances of right spikes properties
rightSpikesProperties = []
# Add 16 spikes to list
for i in range(16):
    rightSpikesProperties.append(SpikesProperties.RightSpike())
    rightSpikesProperties[i - 1].setPositionY((i - 1) * (gameMenuProperties.height / 15))

# Create entity at the middle of the screen
entityProperties = EntitiesProperties.EntityVector()


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
textBounceGame = createText(bounceGameProperties, 70, (58, 58, 64), "Bounce Game")
textBounceGame_rect = textBounceGame.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8))

# Start Game Title
startGameProperties = TextProperties.Text()
textStartGame = createText(startGameProperties, 50, (255, 255, 255), "Start")
textStartGame_rect = textStartGame.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 3))

# Options Title
optionsProperties = TextProperties.Text()
textOptions = createText(optionsProperties, 50, (255, 255, 255), "Options")
textOptions_rect = textOptions.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 4))

# Credits Title
creditsProperties = TextProperties.Text()
textCredits = createText(creditsProperties, 50, (255, 255, 255), "Credits")
textCredits_rect = textCredits.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 5))

# Quit Title
quitProperties = TextProperties.Text()
textQuit = createText(quitProperties, 50, (255, 255, 255), "Quit")
textQuit_rect = textQuit.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 6))

# OPTIONS MENU
backOptionsProperties = TextProperties.Text()
textBackOptions = createText(backOptionsProperties, 40, (255, 255, 255), "Back to lobby")
textBackOptions_rect = textBackOptions.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 7))

# Select skin option
selectOptionsProperties = TextProperties.Text()
textSelectOptions = createText(selectOptionsProperties, 25, (255, 255, 255), "Select")
textSelectOptions_rect = textSelectOptions.get_rect(
    center=(startMenuProperties.width / 3, startMenuProperties.height / 8 * 2.5))

# Select skin option 2
selectOptionsProperties_2 = TextProperties.Text()
textSelectOptions_2 = createText(selectOptionsProperties_2, 25, (255, 255, 255), "Select")
textSelectOptions_2_rect = textSelectOptions_2.get_rect(
    center=(startMenuProperties.width / 3 * 2, startMenuProperties.height / 8 * 2.5))

# Select skin option 3
selectOptionsProperties_3 = TextProperties.Text()
textSelectOptions_3 = createText(selectOptionsProperties_3, 25, (255, 255, 255), "Select")
textSelectOptions_3_rect = textSelectOptions_3.get_rect(
    center=(startMenuProperties.width / 5 * 1, startMenuProperties.height / 8 * 5.5))

# Select skin option 4
selectOptionsProperties_4 = TextProperties.Text()
textSelectOptions_4 = createText(selectOptionsProperties_4, 25, (255, 255, 255), "Select")
textSelectOptions_4_rect = textSelectOptions_4.get_rect(
    center=(startMenuProperties.width / 5 * 2.5, startMenuProperties.height / 8 * 5.5))

# Select skin option 5
selectOptionsProperties_5 = TextProperties.Text()
textSelectOptions_5 = createText(selectOptionsProperties_5, 25, (255, 255, 255), "Select")
textSelectOptions_5_rect = textSelectOptions_5.get_rect(
    center=(startMenuProperties.width / 5 * 4, startMenuProperties.height / 8 * 5.5))

# CREDITS MENU
authorProperties = TextProperties.Text()
textAuthor = createText(authorProperties, 50, (58, 58, 64), "Author")
textAuthor_rect = textAuthor.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8)
)

authorMeProperties = TextProperties.Text()
textAuthorMe = createText(authorMeProperties, 40, (255, 255, 255), "Dawid Kostka")
textAuthorMe_rect = textAuthorMe.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 2)
)

gitHubProperties = TextProperties.Text()
textGitHub = createText(gitHubProperties, 50, (58, 58, 64), "Github")
textGitHub_rect = textGitHub.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 3)
)

myGitHubProperties = TextProperties.Text()
textMyGitHub = createText(myGitHubProperties, 40, (255, 255, 255), "github com TheMissyy")
textMyGitHub_rect = textMyGitHub.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 4)
)

backCreditsProperties = TextProperties.Text()
textBackCredits = createText(backCreditsProperties, 40, (255, 255, 255), "Back to Lobby")
textBackCredits_rect = textBackCredits.get_rect(
    center=(startMenuProperties.getCenterX(), startMenuProperties.height / 8 * 7))

# GAME OVER MENU
# Setting score value
score = 0
# Create new text that show score in the game
scoreProperties = TextProperties.Text()
textScore = createText(scoreProperties, scoreProperties.size, (15, 207, 23), str(score))
textScore_rect = textScore.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() - gameMenuProperties.width / 7))

# Create new text GAME OVER that is visible if player lose
gameOverProperties = TextProperties.Text()
textGameOver = createText(gameOverProperties, 70, (58, 58, 64), "Game Over")
textGameOver_rect = textGameOver.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() - gameMenuProperties.width / 5))

# Create new text Play Again that is visible if player lose
playAgainProperties = TextProperties.Text()
textPlayAgain = createText(playAgainProperties, 40, (255, 255, 255), "Play Again")
textPlayAgain_rect = textPlayAgain.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() + gameMenuProperties.width / 40))

# Create new text Options that is visible if player lose
optionsOverProperties = TextProperties.Text()
textOptionsOver = createText(optionsOverProperties, 40, (255, 255, 255), "Options")
textOptionsOver_rect = textOptionsOver.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() + gameMenuProperties.width / 40 * 4))

# Create new text Back to lobby that is visible if player lose
backLobbyProperties = TextProperties.Text()
textBackLobby = createText(backLobbyProperties, 40, (255, 255, 255), "Back to Lobby")
textBackLobby_rect = textBackLobby.get_rect(
    center=(gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() + gameMenuProperties.width / 40 * 7))

# Current skin of entity
skin = "Circle"
# Creating entity for skin circle
entity = pygame.draw.circle(
    gameScreen,
    entityProperties.entityColor,
    (entityProperties.positionX, entityProperties.positionY),
    entityProperties.size)

# Current menu variable options: Main Menu, Game, Options, Credits
currentMenu = "Main Menu"
# Check if screen should change main menu color in next tick
changeScreenColor = 0
# Variable for smooth gradient in Main Menu
counter = 1

# Declare mouse position to make it global
mousePosition = (-100, -100)

spikesRight = []
spikesLeft = []

blankSpaceRight = [6]
blankSpaceLeft = [random.randrange(0, 11)]


def resetGame():
    global score, gameOver, blankSpaceLeft, blankSpaceRight, entityProperties, textScore
    score = 0
    gameOver = False
    # Reset spikes
    blankSpaceRight = [3]
    blankSpaceLeft = [random.randrange(0, 11)]
    # Reset entity position
    entityProperties = EntitiesProperties.EntityVector()
    entityProperties.setPositionY(gameMenuProperties.height / 2)
    entityProperties.setPositionX(gameMenuProperties.width / 2)
    entityProperties.setSize(entityProperties.defaultSize)
    entityProperties.setSpeed(entityProperties.defaultSpeed)
    entityProperties.setGravity(entityProperties.defaultGravity)
    # Reset score title position and color
    scoreProperties.setColorType(1)
    scoreProperties.setColors(15, 207, 23)
    scoreProperties.refreshColor()
    textScore = createText(scoreProperties, 100, scoreProperties.textColor, str(score))
    # Reset background color
    gameMenuProperties.setColorType(1)
    gameMenuProperties.setColors(45, 237, 53)
    gameMenuProperties.refreshScreenColors()


# clock variable to limit fps in code
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # BALL JUMP OPTIONS
        if currentMenu == "Game" and entityProperties.alive:
            # Check if player use space to jump ball
            if event.type == pygame.KEYDOWN:
                # Checking keyboard and mouse in game
                if event.key == pygame.K_SPACE:
                    entityProperties.setGravity(entityProperties.defaultJumpHeight)
            # Check if player use LMB to jump ball
            if event.type == pygame.MOUSEBUTTONUP:
                entityProperties.setGravity(entityProperties.defaultJumpHeight)

        # BUTTON GLOW
        # If mouse collides with button it glows

        if currentMenu != "Game":
            # Get Mouse potion
            mousePosition = pygame.mouse.get_pos()

            if currentMenu == "Main Menu":
                # Check if player hover Start Game button if do, change color of button
                if textStartGame_rect.collidepoint(mousePosition):
                    textStartGame = createText(startGameProperties, startGameProperties.size, (55, 55, 66), "Start")
                    # Check if player clicked Start Game button Start if it do start game
                    if event.type == pygame.MOUSEBUTTONUP:
                        currentMenu = "Game"
                        resetGame()
                # If player didn't hover Start Game change it color to normal
                else:
                    textStartGame = createText(startGameProperties, startGameProperties.size, (255, 255, 255), "Start")

                # Check if player hover Options button if do, change color of button
                if textOptions_rect.collidepoint(mousePosition):
                    textOptions = createText(optionsProperties, optionsProperties.size, (55, 55, 66), "Options")
                    # Check if player clicked Options button Start if it do move to options menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        currentMenu = "Options"
                # If player didn't hover Options button change it color to normal
                else:
                    textOptions = createText(optionsProperties, optionsProperties.size, (255, 255, 255), "Options")

                # Check if player hover Credits button if do, change color of button
                if textCredits_rect.collidepoint(mousePosition):
                    textCredits = createText(creditsProperties, creditsProperties.size, (55, 55, 66), "Credits")
                    # Check if player clicked Credits button Start if it do move to Credits menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        currentMenu = "Credits"
                # If player didn't hover Credits button change it color to normal
                else:
                    textCredits = createText(creditsProperties, creditsProperties.size, (255, 255, 255), "Credits")

                # Check if player hover Quit button if do, change color of button
                if textQuit_rect.collidepoint(mousePosition):
                    textQuit = createText(quitProperties, quitProperties.size, (55, 55, 66), "Quit")
                    # Check if player clicked Quit button if it do close game
                    if event.type == pygame.MOUSEBUTTONUP:
                        exit(0)
                # If player didn't hover Quit button change it color to normal
                else:
                    textQuit = createText(quitProperties, quitProperties.size, (255, 255, 255), "Quit")

            # Options menu
            elif currentMenu == "Options":

                # Back to lobby button in options menu
                if textBackOptions_rect.collidepoint(mousePosition):
                    textBackOptions = createText(backOptionsProperties, backOptionsProperties.size, (55, 55, 66),
                                                 "Back to lobby")
                    # Check if player clicked PLAY AGAIN button if it do move to Play again menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        currentMenu = "Main Menu"
                # If player didn't hover PLAY AGAIN button change it color to normal
                else:
                    textBackOptions = createText(backOptionsProperties, backOptionsProperties.size, (255, 255, 255),
                                                 "Back to lobby")

                # Select button in options menu
                if textSelectOptions_rect.collidepoint(mousePosition):
                    textSelectOptions = createText(selectOptionsProperties, selectOptionsProperties.size, (55, 55, 66),
                                                   "Select")
                    # Check if player clicked Select button if it do player skin changes
                    if event.type == pygame.MOUSEBUTTONUP:
                        skin = "Circle"
                # If player didn't hover Select button change it color to normal
                else:
                    textSelectOptions = createText(selectOptionsProperties, selectOptionsProperties.size,
                                                   (255, 255, 255),
                                                   "Select")

                # Select 2 button in options menu
                if textSelectOptions_2_rect.collidepoint(mousePosition):
                    textSelectOptions_2 = createText(selectOptionsProperties_2, selectOptionsProperties_2.size,
                                                     (55, 55, 66),
                                                     "Select")
                    # Check if player clicked Select button if it do player skin changes
                    if event.type == pygame.MOUSEBUTTONUP:
                        skin = "Triangle"
                # If player didn't hover Select button change it color to normal
                else:
                    textSelectOptions_2 = createText(selectOptionsProperties_2, selectOptionsProperties_2.size,
                                                     (255, 255, 255),
                                                     "Select")

                # Select 3 button in options menu
                if textSelectOptions_3_rect.collidepoint(mousePosition):
                    textSelectOptions_3 = createText(selectOptionsProperties_3, selectOptionsProperties_3.size,
                                                     (55, 55, 66),
                                                     "Select")
                    # Check if player clicked Select button if it do player skin changes
                    if event.type == pygame.MOUSEBUTTONUP:
                        skin = "Square"
                # If player didn't hover Select button change it color to normal
                else:
                    textSelectOptions_3 = createText(selectOptionsProperties_3, selectOptionsProperties_3.size,
                                                     (255, 255, 255),
                                                     "Select")

                # Select 4 button in options menu
                if textSelectOptions_4_rect.collidepoint(mousePosition):
                    textSelectOptions_4 = createText(selectOptionsProperties_4, selectOptionsProperties_4.size,
                                                     (55, 55, 66),
                                                     "Select")
                    # Check if player clicked Select button if it do player skin changes
                    if event.type == pygame.MOUSEBUTTONUP:
                        skin = "Ruby"
                # If player didn't hover Select button change it color to normal
                else:
                    textSelectOptions_4 = createText(selectOptionsProperties_4, selectOptionsProperties_4.size,
                                                     (255, 255, 255),
                                                     "Select")

                # Select 5 button in options menu
                if textSelectOptions_5_rect.collidepoint(mousePosition):
                    textSelectOptions_5 = createText(selectOptionsProperties_5, selectOptionsProperties_5.size,
                                                     (55, 55, 66),
                                                     "Select")
                    # Check if player clicked Select button if it do player skin changes
                    if event.type == pygame.MOUSEBUTTONUP:
                        skin = "Hexagon"
                # If player didn't hover Select button change it color to normal
                else:
                    textSelectOptions_5 = createText(selectOptionsProperties_5, selectOptionsProperties_5.size,
                                                     (255, 255, 255),
                                                     "Select")

            # Credits menu
            elif currentMenu == "Credits":
                # Back to lobby button in credits menu
                if textBackCredits_rect.collidepoint(mousePosition):
                    textBackCredits = createText(backCreditsProperties, backCreditsProperties.size, (55, 55, 66),
                                                 "Back to lobby")
                    # Check if player clicked PLAY AGAIN button if it do move to Play again menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        currentMenu = "Main Menu"
                # If player didn't hover PLAY AGAIN button change it color to normal
                else:
                    textBackCredits = createText(backCreditsProperties, backCreditsProperties.size, (255, 255, 255),
                                                 "Back to lobby")

            # REFRESH GAME OVER BUTTONS
            elif currentMenu == "Game Over":
                # CHECK BUTTONS AFTER PLAYER LOST
                # Check if player hover Play Again button if do, change color of button
                if textPlayAgain_rect.collidepoint(mousePosition):
                    textPlayAgain = createText(playAgainProperties, playAgainProperties.size, (55, 55, 66),
                                               "Play Again")
                    # Check if player clicked PLAY AGAIN button if it do move to Play again menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        currentMenu = "Game"
                        resetGame()
                # If player didn't hover PLAY AGAIN button change it color to normal
                else:
                    textPlayAgain = createText(playAgainProperties, playAgainProperties.size, (255, 255, 255),
                                               "Play Again")

                # Check if player hover Options button if do, change color of button
                if textOptionsOver_rect.collidepoint(mousePosition):
                    textOptionsOver = createText(optionsOverProperties, optionsOverProperties.size, (58, 58, 64),
                                                 "Options")
                    # Check if player clicked PLAY AGAIN button if it do move to OPTIONS menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        currentMenu = "Options"
                # If player didn't hover OPTIONS button change it color to normal
                else:
                    textOptionsOver = createText(optionsOverProperties, optionsOverProperties.size, (255, 255, 255),
                                                 "Options")

                # Check if player hover BACK TO LOBBY button if do, change color of button
                if textBackLobby_rect.collidepoint(mousePosition):
                    textBackLobby = createText(backLobbyProperties, backLobbyProperties.size, (58, 58, 64),
                                               "Back to Lobby")
                    # Check if player clicked BACK TO LOBBY button if it do move to Main Menu
                    if event.type == pygame.MOUSEBUTTONUP:
                        currentMenu = "Main Menu"
                        startMenuProperties.setColors(gameMenuProperties.colorR,
                                                      gameMenuProperties.colorG,
                                                      gameMenuProperties.colorB)
                        resetGame()
                        # Reset game start option
                # If player didn't hover BACK TO LOBBY button change it color to normal
                else:
                    textBackLobby = createText(backLobbyProperties, backLobbyProperties.size, (255, 255, 255),
                                               "Back to Lobby")

    if currentMenu != "Game Over" and currentMenu != "Game":
        # Dynamic lighting for basic menus
        if currentMenu != "Game Over" and currentMenu != "Game":
            startMenuProperties.dynamicColors(0)
            startMenuProperties.refreshScreenColors()
            gameScreen.fill(startMenuProperties.screenColor)

        # Gradient background in basic menus
        if counter % 15 == 0:
            startMenuProperties.dynamicColors(0)
            startMenuProperties.refreshScreenColors()
            counter = 1
        else:
            counter += 1

        if currentMenu == "Main Menu":
            # Clear every frame
            gameScreen.fill(startMenuProperties.screenColor)

            # Bounce Game title
            gameScreen.blit(textBounceGame, textBounceGame_rect)
            gameScreen.blit(textStartGame, textStartGame_rect)
            gameScreen.blit(textOptions, textOptions_rect)
            gameScreen.blit(textCredits, textCredits_rect)
            gameScreen.blit(textQuit, textQuit_rect)
        # OPTIONS
        elif currentMenu == "Options":
            gameScreen.fill(startMenuProperties.screenColor)
            # Skins title
            gameScreen.blit(textBackOptions, textBackOptions_rect)
            # Circle select option
            pygame.draw.circle(
                gameScreen,
                (255, 255, 255),
                (startMenuProperties.width / 3, startMenuProperties.height / 8 * 1.5),
                startMenuProperties.width / 20)
            gameScreen.blit(textSelectOptions, textSelectOptions_rect)

            # Triangle select option
            pygame.draw.polygon(
                gameScreen,
                (255, 255, 255),
                [(startMenuProperties.width / 3 * 2, startMenuProperties.height / 8 * 2),
                 (startMenuProperties.width / 3 * 2 - startMenuProperties.width / 20,
                  startMenuProperties.height / 8 * 1.5 - startMenuProperties.width / 20),
                 (startMenuProperties.width / 3 * 2 + startMenuProperties.width / 20,
                  startMenuProperties.height / 8 * 1.5 - startMenuProperties.width / 20)]
            )
            gameScreen.blit(textSelectOptions_2, textSelectOptions_2_rect)

            # Square select option
            pygame.draw.rect(
                gameScreen,
                entityProperties.entityColor,
                [startMenuProperties.width / 5 - startMenuProperties.width / 20,
                 startMenuProperties.height / 8 * 4.5 - startMenuProperties.width / 20,
                 startMenuProperties.width / 20 * 2,
                 startMenuProperties.width / 20 * 2
                 ]
            )
            gameScreen.blit(textSelectOptions_3, textSelectOptions_3_rect)

            # Ruby select option
            pygame.draw.polygon(
                gameScreen,
                entityProperties.entityColor,
                [(startMenuProperties.width / 5 * 2.5,
                  startMenuProperties.height / 8 * 4.5 + startMenuProperties.width / 20),
                 (startMenuProperties.width / 5 * 2.5 - startMenuProperties.width / 20,
                  startMenuProperties.height / 8 * 4.5),
                 (startMenuProperties.width / 5 * 2.5,
                  startMenuProperties.height / 8 * 4.5 - startMenuProperties.width / 20),
                 (startMenuProperties.width / 5 * 2.5 + startMenuProperties.width / 20,
                  startMenuProperties.height / 8 * 4.5)],
            )
            gameScreen.blit(textSelectOptions_4, textSelectOptions_4_rect)

            # Hexagon select option
            pygame.draw.polygon(
                gameScreen,
                entityProperties.entityColor,
                [(startMenuProperties.width / 5 * 4 - startMenuProperties.width / 20 / 2,
                  startMenuProperties.height / 8 * 4.5 + startMenuProperties.width / 20 / 1.15),
                 (startMenuProperties.width / 5 * 4 + startMenuProperties.width / 20 / 2,
                  startMenuProperties.height / 8 * 4.5 + startMenuProperties.width / 20 / 1.15),
                 (startMenuProperties.width / 5 * 4 + startMenuProperties.width / 20,
                  startMenuProperties.height / 8 * 4.5),
                 (startMenuProperties.width / 5 * 4 + startMenuProperties.width / 20 / 2,
                  startMenuProperties.height / 8 * 4.5 - startMenuProperties.width / 20 / 1.15),
                 (startMenuProperties.width / 5 * 4 - startMenuProperties.width / 20 / 2,
                  startMenuProperties.height / 8 * 4.5 - startMenuProperties.width / 20 / 1.15),
                 (startMenuProperties.width / 5 * 4 - startMenuProperties.width / 20,
                  startMenuProperties.height / 8 * 4.5),
                 ]
            )
            gameScreen.blit(textSelectOptions_5, textSelectOptions_5_rect)

        # CREDITS
        elif currentMenu == "Credits":
            startScreen.fill(startMenuProperties.screenColor)
            # Author title
            startScreen.blit(textAuthor, textAuthor_rect)
            startScreen.blit(textAuthorMe, textAuthorMe_rect)
            startScreen.blit(textGitHub, textGitHub_rect)
            startScreen.blit(textMyGitHub, textMyGitHub_rect)
            startScreen.blit(textBackCredits, textBackCredits_rect)

    # PLAYER IN GAME
    if currentMenu == "Game":
        # Clear every frame
        gameScreen.fill(gameMenuProperties.screenColor)

        # SHOW SCORE AT SCREEN
        if currentMenu == "Game":
            # If score is 10/100/1000 center it
            if score == 10 or 100 or 1000:
                textScore_rect = textScore.get_rect(
                    center=(
                        gameMenuProperties.getCenterX(),
                        gameMenuProperties.getCenterY() - gameMenuProperties.width / 7))

            # Draw score at screen
            gameScreen.blit(textScore, textScore_rect)

        if entityProperties.size > 0:
            # DRAW ENTITY WITH SKIN
            if skin == "Circle":
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
            elif skin == "Triangle":
                entity = pygame.draw.polygon(
                    gameScreen,
                    entityProperties.entityColor,
                    [(entityProperties.positionX, entityProperties.positionY + entityProperties.size - 4),
                     (entityProperties.positionX - entityProperties.size,
                      entityProperties.positionY - entityProperties.size),
                     (entityProperties.positionX + entityProperties.size,
                      entityProperties.positionY - entityProperties.size)]
                )
            elif skin == "Ruby":
                entity = pygame.draw.polygon(
                    gameScreen,
                    entityProperties.entityColor,
                    [(entityProperties.positionX, entityProperties.positionY + entityProperties.size),
                     (entityProperties.positionX - entityProperties.size, entityProperties.positionY),
                     (entityProperties.positionX, entityProperties.positionY - entityProperties.size),
                     (entityProperties.positionX + entityProperties.size, entityProperties.positionY)],
                )
            elif skin == "Hexagon":
                entity = pygame.draw.polygon(
                    gameScreen,
                    entityProperties.entityColor,
                    [(entityProperties.positionX - entityProperties.size / 2,
                      entityProperties.positionY + entityProperties.size / 1.15),
                     (entityProperties.positionX + entityProperties.size / 2,
                      entityProperties.positionY + entityProperties.size / 1.15),
                     (entityProperties.positionX + entityProperties.size, entityProperties.positionY),
                     (entityProperties.positionX + entityProperties.size / 2,
                      entityProperties.positionY - entityProperties.size / 1.15),
                     (entityProperties.positionX - entityProperties.size / 2,
                      entityProperties.positionY - entityProperties.size / 1.15),
                     (entityProperties.positionX - entityProperties.size, entityProperties.positionY),
                     ]
                )
        # PHYSICS
        # Gravity
        if entityProperties.positionY + entityProperties.size < gameMenuProperties.height:
            entityProperties.setPositionY(entityProperties.positionY + entityProperties.gravitySpeed)
            entityProperties.setGravity(entityProperties.gravitySpeed + entityProperties.defaultGravity / 7)

        # Bouncing
        # If ball don't touch bottom continue
        if entityProperties.positionY < gameMenuProperties.height - entityProperties.size - entityProperties.gravitySpeed:
            if entityProperties.alive:
                # If ball touch top place it under and set default gravity
                if not entityProperties.positionY - entityProperties.size > 0:
                    entityProperties.setPositionY(1 + entityProperties.size)
                    entityProperties.setGravity(entityProperties.defaultGravity / 4)
                # If ball don't touch top continue
                else:
                    if entityProperties.bounceRight:
                        # If ball touch right side change bounce direction
                        if entityProperties.positionX + entityProperties.size >= gameMenuProperties.width:
                            entityProperties.setBounce(False)
                            score += 1
                            # Refresh title
                            textScore = createText(scoreProperties, scoreProperties.size, scoreProperties.textColor,
                                                   str(score))
                            # Change screen color after bounce
                            if score % 4 == 0 and score != 0:
                                changeScreenColor = 100
                            # Change blank space in left side
                            blankSpaceLeft = [random.randrange(0, 11)]

                        # Move ball it to right
                        entityProperties.setPositionX(entityProperties.positionX + entityProperties.speed)
                    else:
                        # If ball touch left side change bounce direction
                        if entityProperties.positionX <= 0 + entityProperties.size:
                            entityProperties.setBounce(True)
                            score += 1
                            textScore = createText(scoreProperties, scoreProperties.size, scoreProperties.textColor,
                                                   str(score))
                            # Change screen color after bounce
                            if score % 4 == 0 and score != 0:
                                changeScreenColor = 100
                            # Change blank space in left side
                            blankSpaceRight = [random.randrange(0, 11)]
                        # Move ball it to left
                        entityProperties.setPositionX(entityProperties.positionX - entityProperties.speed)
            # If player is dead decrease ball size
            else:
                entityProperties.setSize(entityProperties.size - entityProperties.size / 20)
        else:
            # Jump on touch bottom animation
            if entityProperties.alive:
                entityProperties.setGravity(entityProperties.defaultJumpHeight)
                entityProperties.setSpeed(0)
                entityProperties.setAlive(False)
            # Smoothly change size of entity to 0 if it died
            elif not entityProperties.alive:
                if entityProperties.size > 5:
                    entityProperties.setSize(entityProperties.size - entityProperties.size / 20)
                else:
                    currentMenu = "Game Over"

        # Changing color of the screen after player hit 4, 8, 12 points
        if changeScreenColor > 0:
            for i in range(4):
                gameMenuProperties.dynamicColors(0)
                gameMenuProperties.refreshScreenColors()

                scoreProperties.dynamicColors(30)
                scoreProperties.refreshColor()
                # Refresh score title
                textScore = createText(scoreProperties, scoreProperties.size, scoreProperties.textColor,
                                       str(score))
                changeScreenColor -= 1

        # TODO add adjustable space between spikes
        # Create left spikes on the screen
        spikesLeft = []
        for i in range(len(leftSpikesProperties)):
            # If place shouldn have spike draw spike
            if (not i == blankSpaceLeft[0]) and (not i == blankSpaceLeft[0] + 1) and (
                    not i == blankSpaceLeft[0] + 2) and (not i == blankSpaceLeft[0] + 3):
                spikesLeft.append(leftSpikesProperties[i - 1].createSpike(gameScreen))

        # Create right spikes on the screen
        spikesRight = []
        for i in range(len(rightSpikesProperties)):
            # If place shouldn have spike draw spike
            if (not i == blankSpaceRight[0]) and (not i == blankSpaceRight[0] + 1) and (
                    not i == blankSpaceRight[0] + 2) and (not i == blankSpaceRight[0] + 3):
                spikesRight.append(rightSpikesProperties[i - 1].createSpike(gameScreen))

        # Spikes visible Collision with spike
        for i in range(len(spikesRight)):
            if entity.colliderect(spikesRight[i - 1]):
                # If player touch spike he don t have any option to move
                entityProperties.setSpeed(0)
                if entityProperties.alive:
                    entityProperties.setGravity(entityProperties.defaultJumpHeight)
                entityProperties.setAlive(False)

        for i in range(len(spikesLeft)):
            if entity.colliderect(spikesLeft[i - 1]):
                # If player touch spike he don t have any option to move
                entityProperties.setSpeed(0)
                if entityProperties.alive:
                    entityProperties.setGravity(entityProperties.defaultJumpHeight)
                entityProperties.setAlive(False)

    # GAME OVER
    elif currentMenu == "Game Over":
        gameScreen.fill(gameMenuProperties.screenColor)
        # Game over title
        gameScreen.blit(textGameOver, textGameOver_rect)
        gameScreen.blit(textPlayAgain, textPlayAgain_rect)
        gameScreen.blit(textOptionsOver, textOptionsOver_rect)
        gameScreen.blit(textBackLobby, textBackLobby_rect)

        # Refresh your score title
        textScore_rect = textScore.get_rect(
            center=(
                gameMenuProperties.getCenterX(), gameMenuProperties.getCenterY() - gameMenuProperties.width / 10))
        textScore = createText(scoreProperties, 40, (255, 255, 255), ("Your score " + str(score)))
        # Draw your score title at game over screen
        gameScreen.blit(textScore, textScore_rect)

    pygame.display.flip()

    # Limit fps
    clock.tick(60)

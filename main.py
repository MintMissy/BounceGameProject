import pygame

import ScreenProperties

pygame.init()

# Initiation of the window
pygame.display.set_caption("The name of window")
# TODO Setting an icon of program
# pygame.display.set_icon()
# Import screen properties class from file
screenProperties = ScreenProperties.ScreenProperties()
# Set screen size
screen = pygame.display.set_mode((screenProperties.getWidth(), screenProperties.getHeight()))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    screen.fill((screenProperties.getColor()))

    pygame.display.flip()

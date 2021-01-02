# import pygame
#
# pygame.init()
# pygame.display.set_caption("Ball animation :)")
#
# # default screen values
# width = 800
# height = 600
#
# # Starting ball point at middle of the screen
# x = width / 2
# y = height / 2
#
# start = True
#
# speedX = 10  # ball speed x
# speedY = 10  # ball speed y
#
# # Tuple are arrays that are type final
#
# screen = pygame.display.set_mode((width, height))
#
# ball = pygame.image.load('Zadanie2_ball.png')
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit(0)
#
#     screen.fill((15, 15, 15))  # clean screen
#
#     # ZROBIC TO DO ZADANIA 1
#     '''
#     if start == True:
#         screen.fill((15, 15, 15)) #clean screen
#         start = False
#     '''
#
#     def makeBall():
#         a = 5
#
#     screen.blit(ball, (x, y))
#
#     pygame.time.delay(5)
#
#     # That part of script bounce ball if it touch the corner of the screen
#
#     # 44 is ball image X size
#     if x >= width - 44:
#         speedX = -speedX
#     if x <= 0:
#         speedX = -speedX
#
#     # 44 is ball image Y size
#     if y >= height - 44:
#         speedY = -speedY
#     if y <= 0:
#         speedY = -speedY
#
#     pygame.draw.circle(screen, (255, 255, 255), (x + 22, y + 22), 1)
#
#     # Changing position of the ball with speed every tick
#     x += speedX
#     y += speedY
#
#     pygame.display.flip()

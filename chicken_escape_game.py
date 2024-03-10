import pygame

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

#load the background image
background = pygame.image.load('chicken-escape/background.png')

keep_alive = True
while keep_alive:
    #display the background image
    screen.blit(background, [0,0])
    pygame.display.update()
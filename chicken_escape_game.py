import pygame

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

#load the images
background = pygame.image.load('chicken-escape/background.png')
user = pygame.image.load('chicken-escape/user.png')
chicken = pygame.image.load('chicken-escape/chicken.png')
chicken_y = 0

keep_alive = True
clock = pygame.time.Clock()
#game loop
while keep_alive:
    # reset y-coordinate of chicken when it falls out of the screen
    if chicken_y > 600:
        chicken_y = 0
    else:
        chicken_y = chicken_y + 5
    #display the images
    screen.blit(background, [0,0])
    screen.blit(user, [150,520])
    screen.blit(chicken, [0,chicken_y])
    screen.blit(chicken, [150,chicken_y])
    screen.blit(chicken, [280,chicken_y])
    pygame.display.update()
    clock.tick(60)
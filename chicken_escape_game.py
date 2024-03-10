import pygame
import random

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

#load the images
background = pygame.image.load('chicken-escape/background.png')
user = pygame.image.load('chicken-escape/user.png')
chicken = pygame.image.load('chicken-escape/chicken.png')


def random_offset():
    return -1*random.randint(100, 1500)

chicken_y = [random_offset(), random_offset(), random_offset()]
user_x = 150

def update_chicken_position(i):
    if chicken_y[i] > 600:
        chicken_y[i] = random_offset()
    else:
        chicken_y[i] = chicken_y[i] + 5

keep_alive = True
clock = pygame.time.Clock()
#game loop
while keep_alive:
    pygame.event.get()
    keys =  pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        user_x = user_x + 10
    elif keys[pygame.K_LEFT]:
        user_x = user_x - 10
    
    update_chicken_position(0)
    update_chicken_position(1)
    update_chicken_position(2)
    
    
    #display the images
    screen.blit(background, [0,0])
    screen.blit(user, [user_x,520])
    screen.blit(chicken, [0,chicken_y[0]])
    screen.blit(chicken, [150,chicken_y[1]])
    screen.blit(chicken, [280,chicken_y[2]])
    pygame.display.update()
    clock.tick(60)
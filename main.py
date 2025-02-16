import pygame

from GLOBALVARS import *
from GLOBALSPRITE import *

import Collision

pygame.init()

#DISPLAY VARS
BACKGROUNDCOLOR = (0,0,0)
GAMETITLE = "Pong"
TITLEIMAGE = pygame.image.load('titleImage.png')

#RUN VARS
FPS = 60

screen = pygame.display.set_mode(ASPECTRATIO)
screen.fill(BACKGROUNDCOLOR)

pygame.display.set_icon(TITLEIMAGE)
pygame.display.set_caption(GAMETITLE)


#fps:
clock = pygame.time.Clock()

running = True

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    Collision.collideCheck()
    
    BALL.update()
    PADDLE.update()

    

    SPRITEGROUP.draw(screen)

    pygame.display.flip()
    screen.fill(BACKGROUNDCOLOR)

pygame.quit()
from GLOBALSPRITE import * 
from GLOBALVARS import *



def collideCheck ():
    #paddle collision
    if (BALL.rect.colliderect(PADDLE)):
        BALL.updX *= -1

    #wall collision
    if (BALL.rect.topleft[0] <= 0 or BALL.rect.bottomright[0] >= ASPECTRATIO[0]):
        BALL.updX *= -1
        BALL.update()


    if (BALL.rect.topleft [1] <= 0 or BALL.rect.bottomleft[1] >= ASPECTRATIO[1]):
        BALL.updY *= -1
        BALL.update()



    


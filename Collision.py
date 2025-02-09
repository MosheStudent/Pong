from GLOBALSPRITE import * 



def collideCheck ():
    if (BALL.rect.colliderect(PADDLE)):
        BALL.updX *= -1

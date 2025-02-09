import pygame
import random

from GLOBALVARS import *
from GLOBALSPRITE import *

COLOR = (255,255,255)
WIDTH = 5
HEIGHT = 5
POSX = 400
POSY = 400



class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(COLOR)

        pygame.draw.rect(self.image, COLOR, pygame.Rect(0, 0, WIDTH, HEIGHT))
        
        self.rect = self.image.get_rect()
        self.rect.center = (POSX, POSY)

        self.updX = random.randint(-5,5)
        self.updY = random.randint(-5,5)
    
    def update(self):
        if (self.rect.topleft[0] <= 0 or self.rect.bottomright[0] >= ASPECTRATIO[0]):
            self.updX *= -1

        if (self.rect.topleft [1] <= 0 or self.rect.bottomleft[1] >= ASPECTRATIO[1]):
            self.updY *= -1

        self.rect.center = (self.rect.centerx + self.updX, self.rect.centery + self.updY)
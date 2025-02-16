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

        abs = (-1,1)

        self.updX = random.choice(abs) * BALLSPEED
        self.updY = random.choice(abs) * BALLSPEED
    
    def update(self):
        self.rect.center = (self.rect.centerx + self.updX, self.rect.centery + self.updY)
import pygame

#global variables for the sprite
COLOR = (255, 255, 255)
HEIGHT = 50
WIDTH = 10
POSX = 30
POSY = 500

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(COLOR)

        pygame.draw.rect(self.image, COLOR, pygame.Rect(0,0, WIDTH, HEIGHT))

        self.rect = self.image.get_rect()
        self.rect.center = (POSX, POSY)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.centery = mouse_pos[1]
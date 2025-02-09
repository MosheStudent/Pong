import Paddle
import Ball
import pygame

SPRITEGROUP = pygame.sprite.Group()

BALL = Ball.Ball()
SPRITEGROUP.add(BALL)

PADDLE = Paddle.Paddle()
SPRITEGROUP.add(PADDLE)


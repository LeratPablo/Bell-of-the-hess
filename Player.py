import pygame, sys, math
from pygame.locals import *
from SETTINGS import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets\Bell.png").convert_alpha()
        self.scaled_image = pygame.transform.scale(self.image, (64, 64))
        self.pos = pygame.math.Vector2(PLAYER_START_X, PLAYER_START_Y)

        self.speed = PLAYER_SPEED

    def user_input(self):
        self.velX = 0
        self.velY = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.velY = -self.speed
        if keys[pygame.K_DOWN]:
            self.velY = self.speed
        if keys[pygame.K_LEFT]:
            self.velX = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velX = self.speed

        if self.velX != 0 and self.velY != 0:
            self.velX /= math.sqrt(2)
            self.velY /= math.sqrt(2)
    
    def move(self):
        self.pos += pygame.math.Vector2(self.velX, self.velY)
    
    def update(self):
        self.user_input()
        self.move()
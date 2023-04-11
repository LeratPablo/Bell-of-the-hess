import pygame, sys, SETTINGS
from pygame.locals import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('assets/Bell.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
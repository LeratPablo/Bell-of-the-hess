import pygame, sys, math
from pygame.locals import *
from SETTINGS import *
from Player import Player

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.camera_offset

pygame.init()

# Creating the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bell of the childs')
clock = pygame.time.Clock()

# Loads images

player = Player()

def game():
    while True:
        screen.fill((155, 246, 255))
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(player.scaled_image, player.pos)

        player.update()
        pygame.display.update()
        clock.tick(FPS)
game()
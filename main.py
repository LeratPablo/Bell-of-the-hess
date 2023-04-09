import pygame, sys, math, spritesheet
from pygame.locals import *
from SETTINGS import *
from Player import Player

pygame.init()

# Creating the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bell of the childs')
clock = pygame.time.Clock()

# Loads images
player_spritesheet_image = pygame.image.load('assets\BelIdleSpriteSheetl.png').convert_alpha()
player_spritesheet = spritesheet.Spritesheet(player_spritesheet_image)

# player animation frames
player_idle_0 = player_spritesheet.get_image(0, 32, 32, 2, (0, 0, 0))

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
        screen.blit(player_idle_0, (0, 0))
        player.update()
        pygame.display.update()
        clock.tick(FPS)
game()
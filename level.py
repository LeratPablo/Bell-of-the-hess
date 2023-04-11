import pygame, sys
from SETTINGS import *
from tiles import Tile
from player import Player
from debug import debug

class Level:
    
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        
        self.creat_map()
        
    def creat_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == 'X':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                if col == 'P':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
        
    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)
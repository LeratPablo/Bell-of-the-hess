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

        # Idle
        player_idle_0 = pygame.image.load('assets/animations/player/idle/idle_0.png').convert_alpha()
        player_idle_1 = pygame.image.load('assets/animations/player/idle/idle_1.png').convert_alpha()
        player_idle_2 = pygame.image.load('assets/animations/player/idle/idle_2.png').convert_alpha()
        self.player_idle_frames = [player_idle_0, player_idle_1, player_idle_2]
        # Walk down
        player_walkdown_0 = pygame.image.load('assets/animations/player/walkdown/walkdown_0.png').convert_alpha()
        player_walkdown_1 = pygame.image.load('assets/animations/player/walkdown/walkdown_1.png').convert_alpha()
        player_walkdown_2 = pygame.image.load('assets/animations/player/walkdown/walkdown_2.png').convert_alpha()
        player_walkdown_3 = pygame.image.load('assets/animations/player/walkdown/walkdown_3.png').convert_alpha()
        self.player_walkdown_frames = [player_walkdown_0, player_walkdown_1, player_walkdown_2, player_walkdown_3]

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

    def animation_controller(self):
        current_frame = 0
        frame = None
        if keys[pygame.K_UP]:
            pass
        elif keys[pygame.K_DOWN]:
            max_frame = len(self.player_walkdown_frames)
            frame = self.player_walkdown_frames[current_frame]
        elif keys[pygame.K_LEFT]:
            pass
        elif keys[pygame.K_RIGHT]:
            pass
        else:
            max_frame = len(self.player_idle_frames)
            
        
        if current_frame >= max_frame:
            current_frame = 0
        else:
            current_frame +=1
        
        return frame
    
    def move(self):
        self.pos += pygame.math.Vector2(self.velX, self.velY)
    
    def update(self):
        self.user_input()
        self.move()
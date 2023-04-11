import pygame, sys, math
from pygame.locals import *
from SETTINGS import *
from player import Player

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.camera_offset

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

pygame.init()

# Creating the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bell of the childs')
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

# Loads images

player = Player()

def main_menu():
    while True:
        screen.fill((0, 0, 0))
        draw_text('Main menu', font, (255, 255, 255), screen, 20, 20)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        # buttons creation
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mouse_x, mouse_y)) and click:
            game()
        if button_2.collidepoint((mouse_x, mouse_y)) and click:
            pygame.quit()
            sys.exit()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                click = True

        pygame.display.update()
        clock.tick(60)

def game():
    running = True
    while running:
        screen.fill((155, 246, 255))
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False

        screen.blit(player.image, player.pos)

        player.update()
        pygame.display.update()
        clock.tick(FPS)

main_menu()
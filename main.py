import pygame, sys
from SETTINGS import *
from level import Level

class Game:
    
    def __init__(self):
        
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Bell of the wild')
        self.clock = pygame.time.Clock()
        
        self.level = Level()
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
            
            self.screen.fill((0, 0, 0))
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
            
if __name__ == '__main__':
    game = Game()
    game.run()
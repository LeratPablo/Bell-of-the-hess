import pygame, sys
from sprites import *
from settings import *

class Game:
    def __init__(self):
        pygame.init()

        self.scren = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 32)
        self.running = True

        self.character_spritesheet = Spritesheet('assets/player_spritesheet.png')
        self.terrain_spritesheet = Spritesheet('assets/block_spritsheet.png')
        self.enemy_spritesheet = Spritesheet('assets/ennemy_spritesheet.png')

    def createTilemap(self):
        for i, row in enumerate(WORLD_MAP):
            for j, col in enumerate(row):
                Grass(self, j, i)
                if col == 'W':
                    Block(self, j, i)
                if col == 'P':
                    Player(self, j, i)
                if col == 'E':
                    Enemy(self, j, i)

    def new(self):
        # New game
        self.playing = True

        # Create group of sprites
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()

    def events(self):
        '''
            Contain every key pressed event
        '''
        # Game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        '''
            Update the game
        '''
        # Game loop update
        self.all_sprites.update()

    def draw(self):
        '''
            Display all the sprites on the screen
        '''
        # Game loop draw
        self.scren.fill(BLACK)
        self.all_sprites.draw(self.scren)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # Game loop

        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    
    def game_over(self):
        pass
    
    def intro_screen(self):
        intro = True

        title = self.font.render('Bell of the wild', True, BLACK)
        title_rect = title.get_rect(x=1, y=1)
        play_button = Button(10, 50, 100, 50, WHITE, BLACK, 'Play', 32)
        
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            # self.scren.blit(self.intro_background, (0, 0))
            self.scren.fill((255, 0, 0))
            self.scren.blit(title, title_rect)
            self.scren.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)

            pygame.display.update()
    
g = Game()
g.intro_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
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
        
        self.win = False

        self.character_spritesheet = Spritesheet('assets/player_spritesheet.png')
        self.enemy_spritesheet = Spritesheet('assets/ennemy_spritesheet.png')
        self.teacher_spritesheet = Spritesheet('assets/teacher_spritesheet.png')
        self.sad_child_spritesheet = Spritesheet('assets/sadchild_spritesheet.png')
        self.terrain_spritesheet = Spritesheet('assets/block_spritsheet.png')
        self.player_interaction_spritesheet = Spritesheet('assets/player_interaction-Sheet.png')
        self.enemies_vanish = Spritesheet('assets/enemy_vanish_spritesheet.png')

    def createTilemap(self):
        for i, row in enumerate(WORLD_MAP):
            for j, col in enumerate(row):
                Grass(self, j, i)
                if col == 'W':
                    Block(self, j, i)
                if col == 'P':
                    Player(self, j, i)
                if col == 'P':
                    PlayerInteraction(self, j, i)
                if col == 'E':
                    Enemy(self, j, i)
                # if col == 'E':
                #     EnemyVanish(self, j, i)
                if col == 'T':
                    Teacher(self, j, i)
                if col == 'S':
                    SadChild (self, j, i)
                if col == 'F':
                    Sand(self, j, i)

    def new(self):
        # New game
        self.playing = True

        # Create group of sprites
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.teacher = pygame.sprite.LayeredUpdates()
        self.sad_child = pygame.sprite.LayeredUpdates()
        self.player_interaction = pygame.sprite.LayeredUpdates()
        self.enemy_vanish = pygame.sprite.LayeredUpdates()

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
        if len(g.sad_child) == 0 and len(g.enemies) == 0:
            self.win = True
            self.playing = False

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

    def intro_screen(self):
        intro = True

        title = self.font.render('Bell of the hess', True, WHITE)
        title_rect = title.get_rect(x=(WIN_WIDTH/2)-title.get_rect().width/2, y=(WIN_HEIGHT/2)-100)
        play_button = Button((WIN_WIDTH/2)-50, (WIN_HEIGHT/2), 100, 50, WHITE, BLACK, 'Play', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.scren.fill((0, 0, 0))
            self.scren.blit(title, title_rect)
            self.scren.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)

            pygame.display.update()

    def game_over(self):
        game_over = True

        title = self.font.render('Game over', True, WHITE)
        title_rect = title.get_rect(x=(WIN_WIDTH/2)-title.get_rect().width/2, y=(WIN_HEIGHT/2)-100)
        retry_button = Button((WIN_WIDTH/2)-50, (WIN_HEIGHT/2), 100, 50, WHITE, BLACK, 'Retry', 32)

        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if retry_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            self.scren.fill((0, 0, 0))
            self.scren.blit(title, title_rect)
            self.scren.blit(retry_button.image, retry_button.rect)
            self.clock.tick(FPS)

            pygame.display.update()

    def win_screen(self):
        winning = True

        title = self.font.render('You win', True, WHITE)
        title_rect = title.get_rect(x=(WIN_WIDTH/2)-title.get_rect().width/2, y=(WIN_HEIGHT/2)-100)
        leave = Button((WIN_WIDTH/2)-50, (WIN_HEIGHT/2), 100, 50, WHITE, BLACK, 'Leave', 32)

        while winning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    winning = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            
            if leave.is_pressed(mouse_pos, mouse_pressed):
                pygame.quit()
                sys.exit()

            self.scren.fill((0, 0, 0))
            self.scren.blit(title, title_rect)
            self.scren.blit(leave.image, leave.rect)
            self.clock.tick(FPS)

            pygame.display.update()

g = Game()
g.intro_screen()
g.new()

while g.running:

    g.main()
    if g.win:
        g.win_screen()
        break
    g.game_over()

pygame.quit()
sys.exit()
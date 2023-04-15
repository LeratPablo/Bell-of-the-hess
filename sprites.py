import pygame, math, random
from settings import *

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.player
        
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILES_SIZE
        self.y = y * TILES_SIZE
        self.width = TILES_SIZE
        self.height = TILES_SIZE
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = 'down'
        self.animation_loop = 0

        self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()
        
        self.rect.x += self.x_change
        self.collision('x')
        self.rect.y += self.y_change
        self.collision('y')
        
        self.x_change = 0
        self.y_change = 0
    
    def movement(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'
            
    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.playing = False
            
    def collision(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    
    def animate(self):
        down_animation = [
            self.game.character_spritesheet.get_sprite(0, 32, self.width, self.height),
            self.game.character_spritesheet.get_sprite(32,32, self.width, self.height),
            self.game.character_spritesheet.get_sprite(64, 32, self.width, self.height),
            self.game.character_spritesheet.get_sprite(96, 32, self.width, self.height)
        ]
        up_animation = [
            self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height),
            self.game.character_spritesheet.get_sprite(32,64, self.width, self.height),
            self.game.character_spritesheet.get_sprite(64, 64, self.width, self.height),
            self.game.character_spritesheet.get_sprite(96, 64, self.width, self.height)
        ]
        left_animation = [
            self.game.character_spritesheet.get_sprite(0, 96, self.width, self.height),
            self.game.character_spritesheet.get_sprite(32,96, self.width, self.height),
            self.game.character_spritesheet.get_sprite(64, 96, self.width, self.height),
            self.game.character_spritesheet.get_sprite(96, 96, self.width, self.height)
        ]
        right_animation = [
            self.game.character_spritesheet.get_sprite(0, 128, self.width, self.height),
            self.game.character_spritesheet.get_sprite(32,128, self.width, self.height),
            self.game.character_spritesheet.get_sprite(64, 128, self.width, self.height),
            self.game.character_spritesheet.get_sprite(96, 128, self.width, self.height)
        ]
        idle_animation = [
            self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(32,0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(64, 0, self.width, self.height)
        ]
        
        if self.facing == 'down':
            if self.y_change == 0:
                # self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
                if self.animation_loop >= 3:
                    self.animation_loop = 0
                self.image = idle_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.08
            else:
                if self.animation_loop >= 4:
                    self.animation_loop = 0
                self.image = down_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.15

        if self.facing == 'up':
            if self.y_change == 0:
                # self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
                if self.animation_loop >= 3:
                    self.animation_loop = 0
                self.image = idle_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.08
            else:
                if self.animation_loop >= 4:
                    self.animation_loop = 0
                self.image = up_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.15

        if self.facing == 'left':
            if self.x_change == 0:
                # self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
                if self.animation_loop >= 3:
                    self.animation_loop = 0
                self.image = idle_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.08
            else:
                if self.animation_loop >= 4:
                    self.animation_loop = 0
                self.image = left_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.15

        if self.facing == 'right':
            if self.x_change == 0:
                # self.image = self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height)
                if self.animation_loop >= 3:
                    self.animation_loop = 0
                self.image = idle_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.08
            else:
                if self.animation_loop >= 4:
                    self.animation_loop = 0
                self.image = right_animation[math.floor(self.animation_loop)]
                self.animation_loop += 0.15

class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILES_SIZE
        self.y = y * TILES_SIZE
        self.width = TILES_SIZE
        self.height = TILES_SIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(32, 0, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class Grass(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILES_SIZE
        self.y = y * TILES_SIZE
        self.width = TILES_SIZE
        self.height = TILES_SIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(64, 96, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Sand(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * TILES_SIZE
        self.y = y * TILES_SIZE
        self.width = TILES_SIZE
        self.height = TILES_SIZE
        
        self.image = self.game.terrain_spritesheet.get_sprite(96, 32, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILES_SIZE
        self.y = y * TILES_SIZE
        self.width = TILES_SIZE
        self.height = TILES_SIZE
        
        self.x_change = 0
        self.y_change = 0
        
        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 0
        self.movement_loop = 0
        self.max_travel = random.randint(7, 30)
        
        self.angry = True
        self.can_tp = True

        self.timer = 0
        self.slow_timer = 0
        self.cooldown = 4
        self.on_cooldown = False
        self.state = 'idle'
        
        self.image = self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        
    def update(self):
        self.player_interact()
        self.teacher_interaction()
        if not self.angry and self.can_tp:
            self.to_sandbox((random.randint(1125, 1240) / 32), (random.randint(540, 666) / 32))
            self.can_tp = False

        self.animate()
        self.movement()
        self.rect.x += self.x_change
        self.collision('x')
        self.rect.y += self.y_change
        self.collision('y')

        self.x_change = 0
        self.y_change = 0
    
    def collision(self, direction):
        if direction == 'x':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        if direction == 'y':
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    
    def teacher_interaction(self):
        hits = pygame.sprite.spritecollide(self, self.game.teacher, False)
        
        if hits:
            self.angry = False
            
    def player_interact(self):
        for p in self.game.player:
                player_pos = p.rect.center
        enemy_pos = self.rect.center
        distance = math.sqrt((player_pos[0] - enemy_pos[0])**2 + (player_pos[1] - enemy_pos[1])**2)
        keys = pygame.key.get_pressed()
        
        if distance <= INTERACT_RADIUS and keys[pygame.K_SPACE] and not self.on_cooldown:
            self.state = 'slowed'
            self.on_cooldown = True
        if self.on_cooldown:
            self.timer += (1/60)*4
            if self.timer >= self.cooldown:
                self.timer = 0
                self.on_cooldown = False
                
        if not self.on_cooldown:
            print('pret')
        else:
            print("pas pret")

    def to_sandbox(self, x, y):
        self.kill()
        SadChild(self.game, x, y)

    def movement(self):
        if self.angry:
            cd = 1.5
            if self.state == 'slowed':
                self.slow_timer += 1/60
                if self.slow_timer >= cd:
                    self.slow_timer = 0
                    self.state = 'not slowed'
            for p in self.game.player:
                player_pos = p.rect.center

            enemy_pos = self.rect.center
            distance = math.sqrt((player_pos[0] - enemy_pos[0])**2 + (player_pos[1] - enemy_pos[1])**2)

            if distance <= CHASE_RADIUS:
                if player_pos[0] > enemy_pos[0]:
                    if self.state == 'slowed' and self.slow_timer < cd:
                        self.x_change += SLOWED_DOWN_ENEMY_SPEED
                    else:
                        self.x_change += CHASE_ENEMY_SPEED
                    self.facing = 'right'
                elif player_pos[0] < enemy_pos[0]:
                    if self.state == 'slowed' and self.slow_timer < cd:
                        self.x_change -= SLOWED_DOWN_ENEMY_SPEED
                    else:
                        self.x_change -= CHASE_ENEMY_SPEED
                    self.facing = 'left'

                if player_pos[1] > enemy_pos[1]:
                    if self.state == 'slowed' and self.slow_timer < cd:
                        self.y_change += SLOWED_DOWN_ENEMY_SPEED
                    else:
                        self.y_change += CHASE_ENEMY_SPEED
                    self.facing = 'down'
                elif player_pos[1] < enemy_pos[1]:
                    if self.state == 'slowed' and self.slow_timer < cd:
                        self.y_change -= SLOWED_DOWN_ENEMY_SPEED
                    else:
                        self.y_change -= CHASE_ENEMY_SPEED
                    self.facing = 'up'
            else:
                # self.state = 'idle'
                if self.facing == 'up' or self.facing == 'down':
                    self.facing = random.choice(['left', 'right'])
                if self.facing == 'left':
                    self.x_change -= IDLE_ENEMY_SPEED
                    self.movement_loop -= 1
                    if self.movement_loop <= -self.max_travel:
                        self.facing = 'right'

                if self.facing == 'right':
                    self.x_change += IDLE_ENEMY_SPEED
                    self.movement_loop += 1
                    if self.movement_loop >= self.max_travel:
                        self.facing = 'left'

    def animate(self):
        down_animation = [
            self.game.enemy_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.enemy_spritesheet.get_sprite(32,0, self.width, self.height)
        ]
        up_animation = [
            self.game.enemy_spritesheet.get_sprite(0, 32, self.width, self.height),
            self.game.enemy_spritesheet.get_sprite(32,32, self.width, self.height)
        ]
        left_animation = [
            self.game.enemy_spritesheet.get_sprite(0, 64, self.width, self.height),
            self.game.enemy_spritesheet.get_sprite(32,64, self.width, self.height)
        ]
        right_animation = [
            self.game.enemy_spritesheet.get_sprite(0, 96, self.width, self.height),
            self.game.enemy_spritesheet.get_sprite(32,96, self.width, self.height)
        ]
        
        if self.facing == 'left':
            if self.animation_loop >= 2:
                self.animation_loop = 0
            self.image = left_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1

        if self.facing == 'right':
            if self.animation_loop >= 2:
                self.animation_loop = 0
            self.image = right_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1

        if self.facing == 'down':
            if self.animation_loop >= 2:
                self.animation_loop = 0
            self.image = down_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1

        if self.facing == 'up':
            if self.animation_loop >= 2:
                self.animation_loop = 0
            self.image = up_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1

class Button:
    def __init__(self, x,y, width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font(None, fontsize)
        self.content = content
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self.fg = fg
        self.bg = bg
        
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        self.text = self.font.render(self.content, True, self.fg)
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)
        
    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False

class Teacher(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.teacher
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILES_SIZE
        self.y = y * TILES_SIZE
        self.width = TILES_SIZE
        self.height = TILES_SIZE
        
        self.x_change = 0
        self.y_change = 0

        self.animation_loop = 0

        self.image = self.game.teacher_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()

    # def enemy_collide(self):
    #     hits = 

    def animate(self):
        idle_animation = [
            self.game.teacher_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.teacher_spritesheet.get_sprite(32,0, self.width, self.height)
        ]

        if self.animation_loop >= 2:
            self.animation_loop = 0
        self.image = idle_animation[math.floor(self.animation_loop)]
        self.animation_loop += 0.1

class SadChild(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = SAD_CHILD
        self.groups = self.game.all_sprites, self.game.sad_child
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILES_SIZE
        self.y = y * TILES_SIZE
        self.width = TILES_SIZE
        self.height = TILES_SIZE
        
        self.x_change = 0
        self.y_change = 0

        self.animation_loop = 0
        
        self.state = 'sad'

        self.image = self.game.sad_child_spritesheet.get_sprite(0, 0, self.width, self.height)
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
        self.player_interaction()
        
    def player_interaction(self):
        for p in self.game.player:
                player_pos = p.rect.center
        sad_child_pos = self.rect.center
        distance = math.sqrt((player_pos[0] - sad_child_pos[0])**2 + (player_pos[1] - sad_child_pos[1])**2)
        keys = pygame.key.get_pressed()
        
        if distance < INTERACT_RADIUS and keys[pygame.K_SPACE]:
            self.state = 'happy'

    def animate(self):
        sad_animation = [
            self.game.sad_child_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.sad_child_spritesheet.get_sprite(32,0, self.width, self.height)
        ]
        happy_animation = [
            self.game.sad_child_spritesheet.get_sprite(0, 32, self.width, self.height),
            self.game.sad_child_spritesheet.get_sprite(32,32, self.width, self.height)
        ]

        if self.state == 'sad':
            if self.animation_loop >= 2:
                self.animation_loop = 0
            self.image = sad_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
        else:
            if self.animation_loop >= 2:
                self.animation_loop = 0
            self.image = happy_animation[math.floor(self.animation_loop)]
            self.animation_loop += 0.1


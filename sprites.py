import pygame
import pyganim
import random
import math

enemy_lv1 = [('Enemy1/Frame0.png', 0.01),
             ('Enemy1/Frame1.png', 0.01),
             ('Enemy1/Frame2.png', 0.01),
             ('Enemy1/Frame3.png', 0.01),
             ('Enemy1/Frame4.png', 0.01),
             ('Enemy1/Frame5.png', 0.01),
             ('Enemy1/Frame6.png', 0.01),
             ('Enemy1/Frame8.png', 0.01),
             ('Enemy1/Frame9.png', 0.01),
             ('Enemy1/Frame10.png', 0.01),
             ('Enemy1/Frame11.png', 0.01),
             ('Enemy1/Frame12.png', 0.01),
             ('Enemy1/Frame13.png', 0.01),
             ('Enemy1/Frame14.png', 0.01),
             ('Enemy1/Frame15.png', 0.01),
             ('Enemy1/Frame16.png', 0.01),
             ('Enemy1/Frame17.png', 0.01)]

enemy_lv2 = [('Enemy2/Frame0.png', 0.01),
             ('Enemy2/Frame1.png', 0.01),
             ('Enemy2/Frame2.png', 0.01),
             ('Enemy2/Frame3.png', 0.01),
             ('Enemy2/Frame4.png', 0.01),
             ('Enemy2/Frame5.png', 0.01),
             ('Enemy2/Frame6.png', 0.01),
             ('Enemy2/Frame8.png', 0.01),
             ('Enemy2/Frame9.png', 0.01),
             ('Enemy2/Frame10.png', 0.01),
             ('Enemy2/Frame11.png', 0.01),
             ('Enemy2/Frame12.png', 0.01),
             ('Enemy2/Frame13.png', 0.01),
             ('Enemy2/Frame14.png', 0.01),
             ('Enemy2/Frame15.png', 0.01),
             ('Enemy2/Frame16.png', 0.01),
             ('Enemy2/Frame17.png', 0.01)]

shockwave = pyganim.PygAnimation([('Shockwave/Frame1.png', 0.01),
                                  ('Shockwave/Frame2.png', 0.01),
                                  ('Shockwave/Frame3.png', 0.01),
                                  ('Shockwave/Frame4.png', 0.01),
                                  ('Shockwave/Frame5.png', 0.01),
                                  ('Shockwave/Frame6.png', 0.01),
                                  ('Shockwave/Frame7.png', 0.01),
                                  ('Shockwave/Frame8.png', 0.01),
                                  ('Shockwave/Frame9.png', 0.01),
                                  ('Shockwave/Frame10.png', 0.01),
                                  ('Shockwave/Frame11.png', 0.01),
                                  ('Shockwave/Frame12.png', 0.01),
                                  ('Shockwave/Frame13.png', 0.01),
                                  ('Shockwave/Frame14.png', 0.01),
                                  ('Shockwave/Frame15.png', 0.01),
                                  ('Shockwave/Frame16.png', 0.01),
                                  ('Shockwave/Frame17.png', 0.01),
                                  ('Shockwave/Frame18.png', 0.01),
                                  ('Shockwave/Frame19.png', 0.01),
                                  ('Shockwave/Frame20.png', 0.01),
                                  ('Shockwave/Frame21.png', 0.01),
                                  ('Shockwave/Frame22.png', 0.01),
                                  ('Shockwave/Frame23.png', 0.01),
                                  ('Shockwave/Frame24.png', 0.01),
                                  ('Shockwave/Frame25.png', 0.01),
                                  ('Shockwave/Frame26.png', 0.01),
                                  ('Shockwave/Frame27.png', 0.01),
                                  ('Shockwave/Frame28.png', 0.01),
                                  ('Shockwave/Frame29.png', 0.01),
                                  ('Shockwave/Frame30.png', 0.01)])
shockwave.rate = 0.5
shockwave.loop = False


def angle_to_mouse(location):
    mouse_X, mouse_Y = pygame.mouse.get_pos()
    player_X, player_Y = location
    return math.atan2(mouse_X-player_X, mouse_Y-player_Y)


def angle_to_player(location, player):
    X, Y = location
    player_X, player_Y = player
    return math.atan2(player_X - X, player_Y - Y)


def calculate_angular_movement(old_pos, angle, speed):
    old_x, old_y = old_pos
    moved_x = math.sin(angle) * speed
    moved_y = math.cos(angle) * speed
    return (old_x + moved_x, old_y + moved_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.anim1 = pyganim.PygAnimation([('Player/Frame0.png', 0.01),
                                           ('Player/Frame1.png', 0.01),
                                           ('Player/Frame2.png', 0.01),
                                           ('Player/Frame3.png', 0.01),
                                           ('Player/Frame4.png', 0.01),
                                           ('Player/Frame5.png', 0.01),
                                           ('Player/Frame6.png', 0.01),
                                           ('Player/Frame7.png', 0.01),
                                           ('Player/Frame8.png', 0.01),
                                           ('Player/Frame9.png', 0.01),
                                           ('Player/Frame10.png', 0.01),
                                           ('Player/Frame11.png', 0.01),
                                           ('Player/Frame12.png', 0.01),
                                           ('Player/Frame13.png', 0.01),
                                           ('Player/Frame14.png', 0.01),
                                           ('Player/Frame15.png', 0.01),
                                           ('Player/Frame16.png', 0.01),
                                           ('Player/Frame17.png', 0.01),
                                           ('Player/Frame18.png', 0.01),
                                           ('Player/Frame19.png', 0.01),
                                           ('Player/Frame20.png', 0.01),
                                           ('Player/Frame21.png', 0.01),
                                           ('Player/Frame22.png', 0.01)])
        self.anim1.play()
        self.anim1.rate = 0.25
        self.anim2 = pyganim.PygAnimation([('Player/Frame23.png', 0.01),
                                           ('Player/Frame24.png', 0.01),
                                           ('Player/Frame25.png', 0.01),
                                           ('Player/Frame26.png', 0.01),
                                           ('Player/Frame27.png', 0.01),
                                           ('Player/Frame28.png', 0.01),
                                           ('Player/Frame29.png', 0.01),
                                           ('Player/Frame30.png', 0.01),
                                           ('Player/Frame31.png', 0.01),
                                           ('Player/Frame32.png', 0.01),
                                           ('Player/Frame33.png', 0.01),
                                           ('Player/Frame34.png', 0.01),
                                           ('Player/Frame35.png', 0.01),
                                           ('Player/Frame36.png', 0.01),
                                           ('Player/Frame37.png', 0.01),
                                           ('Player/Frame38.png', 0.01),
                                           ('Player/Frame39.png', 0.01),
                                           ('Player/Frame40.png', 0.01)])
        self.anim2.play()
        self.anim2.rate = 0.25
        self.image = pygame.image.load('./Player/Middle.png').convert_alpha()
        self.shadow = pygame.image.load('.//Player/Shadow.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.shadowrect = self.shadow.get_rect()
        self.rect.center = position
        self.life = 3


class Projectile(pygame.sprite.Sprite):
    def __init__(self, position):

        pygame.sprite.Sprite.__init__(self)
        self.co = position
        self.image = pygame.image.load('./Textures/Projectile.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.co
        self.direction = angle_to_mouse(self.co)
        self.time = 0


class Enemy(pygame.sprite.Sprite):
    def __init__(self, position, lives, anim, movement):

        pygame.sprite.Sprite.__init__(self)
        self.anim = pyganim.PygAnimation(anim)
        self.anim.play()
        if random.randint(0,1) == 1:
            self.anim.rate = 0.25
        else:
            self.anim.rate = 0.25
            self.anim.reverse()
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.rect.center = position
        self.life = lives
        self.score = lives
        self.co = position
        self.offset = movement


class Powerup(pygame.sprite.Sprite):
    def __init__(self, position, duration):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./Player/Shadow.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.X, self.Y = position
        self.rect.center = position
        self.timer = duration






import pygame, sys

class Anim:
    def __init__(self, pos_x, pos_y):
        self.attack_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load(r'anim\h1.png'))
        self.sprites.append(pygame.image.load(r'anim\h2.png'))
        self.sprites.append(pygame.image.load(r'anim\h3.png'))
        self.sprites.append(pygame.image.load(r'anim\h4.png'))
        self.sprites.append(pygame.image.load(r'anim\h5.png'))
        self.sprites.append(pygame.image.load(r'anim\h6.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def attack(self):
        self.attack_animation = True

    def update(self, speed):
        if self.attack_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.attack_animation = False

        self.image = self.sprites[int(self.current_sprite)]




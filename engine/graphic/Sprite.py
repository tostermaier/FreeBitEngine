import pygame


class Sprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        print("sprite initialized")

    def draw_sprite(self, color):
        self.image = pygame.Surface([32,32])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        return self.image
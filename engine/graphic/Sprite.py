import pygame


class Sprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        print("sprite initialized")

    def draw_sprite_color(self, color):
        self.image = pygame.Surface([32,32])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        return self.image

    def draw_sprite_image(self, image_path,scale_x, scale_y):

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(scale_x,scale_y))
        self.rect = self.image.get_rect()
        return self.image
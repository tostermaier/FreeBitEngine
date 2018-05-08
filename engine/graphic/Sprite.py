import pygame


class Sprite:
    x = 10
    y =0
    rect =pygame.Rect((0,0,0,0))
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        print("sprite initialized")
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self,x):
        self.x = x

    def set_y(self,y):
        self.y = y

    def draw_sprite_color(self, color):
        self.image = pygame.Surface([32,32])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        return self.image

    def draw_sprite_image(self, image_path,scale_x, scale_y):

        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image,(scale_x,scale_y))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        print(self.rect)
        return self.image

    def get_sprite_rect(self):
        return self.rect

    def collider_enter(self, obj):
        if (self.rect.colliderect(obj)):
            print("hit me")


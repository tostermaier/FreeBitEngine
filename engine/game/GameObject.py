from engine.game.Collider import Collider
from engine.graphic import Sprite


class GameObject(Collider):

    sprite = Sprite.Sprite
    def __init__(self):
        self.set_pos_x(10)
        self.set_pos_y(10)

    def move_object(self, x, y):
        self.set_pos_x(self,x)
        self.set_pos_y(self,y)
        return self.sprite.draw_sprite(self,(64, 64, 64))

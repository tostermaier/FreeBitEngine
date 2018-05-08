from engine.graphic.Sprite import Sprite



class GameObject(Sprite):

    def __init__(self):
       pass


    def move_object(self, speed_x, y):
        self.set_x(self,self.x+100*(speed_x/1000))


    def update(self):
      return  self.draw_sprite_color(self,(64, 64, 64))

    def get_position(self):
        return (self.get_x(self),self.get_y(self))
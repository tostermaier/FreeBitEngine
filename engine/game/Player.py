from engine.game.GameObject import GameObject
from engine.graphic.Animation import Animation
import pygame


class Player(GameObject):

    walk_sprite= ['Sprites\Character\char_walk_1.png','Sprites\Character\char_walk_2.png']
    walk = False
    current_sprite = 'Sprites\Character\char_idle_1.png'
    animation_state = 0
    move_int = 0
    animation = Animation()
    animation.set_sprites(walk_sprite)
    def __init__(self):
        pass




    def setup(self):
     #   self.setup_collider(self,64,64,self.get_pos_x(self),self.get_pos_y(self))
        pass


    def input(self, timestep):

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_d]:
                    self.move_object(self,30,0)

                    print(self.rect.x)
                   # self.move_object(self,self.get_rect_position((self)+100*timestep),self.get_pos_y(self))
                   # self.set_pos_x(self,self.get_pos_x(self)+100*timestep)
                    self.walk = True
            else:
                self.walk = False



    def play_walk_animation(self):
        self.animation.play_animation(0.3)
        return self.animation.get_current_sprite()

    def update(self, timestep):
        self.input(self,timestep)
        if (self.walk == True):

            self.current_sprite = self.play_walk_animation(self)
        self.rect.x +=1
        print(self.rect)
        return self.draw_sprite_image(self,self.current_sprite, 64, 64)

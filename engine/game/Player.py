from engine.game.GameObject import GameObject
import pygame


class Player(GameObject):
    walk_sprite= ['Sprites\Character\char_walk_1.png','Sprites\Character\char_walk_2.png']
    walk = False
    current_sprite = 'Sprites\Character\char_idle_1.png'
    animation_state = 0
    def __init__(self):
        pass

    def setup(self):
        pass

    def input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_d]:
                    self.set_pos_x(self,self.get_pos_x(self)+1)
                    self.walk = True
            else:
                self.walk = False

    def animation(self):
        if(self.animation_state<len(self.walk_sprite)):

            self.animation_state += 1
            print("check")
        else:
           
            print(self.animation_state)
        print(self.walk)
        self.current_sprite = self.walk_sprite[self.animation_state]
    def update(self):

        self.input(self)
        if (self.walk == True):
            self.animation(self)
        return self.sprite.draw_sprite_image(self,self.current_sprite, 64, 64)

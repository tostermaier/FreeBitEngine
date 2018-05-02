from engine.graphic.Sprite import Sprite


class Animation:
    animation_state = 0
    sprite = Sprite
    sprites = []
    current_sprite = 'Sprites\Character\char_idle_1.png'
    animation_timer = 0

    def __init__(self):
        pass

    def get_sprites(self):
        return self.sprites

    def set_sprites(self,sprites):
        self.sprites = sprites
    def get_sprite_from_sprites(self,sprite_num):
        return self.sprites[sprite_num]

    def get_current_sprite(self):
        return self.current_sprite

    def set_current_sprite(self,sprite):
        self.current_sprite = sprite

    def get_animation_state(self):
        return self.animation_state

    def set_animation_state(self,state):
        self.animation_state = state

    def play_animation(self,timing):
        self.animation_timer += timing
        if( self.animation_timer >= 1):

            if( self.get_animation_state()<len(self.get_sprites())):
                self.set_current_sprite(self.get_sprite_from_sprites(self.get_animation_state()))
                self.set_animation_state(self.get_animation_state() + 1)


            else:
                self.set_animation_state(0)

            self.animation_timer = 0

        return self.current_sprite
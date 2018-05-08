import pygame
from engine.graphic import Sprite
from engine.game import GameObject
from engine.game import Player

player = Player.Player
class WindowFrame:
    sprite = Sprite.Sprite()
    obj = GameObject.GameObject
  #  player.setup_animation_controller(player)

    def update(self):
        pygame.init()
      #  player.setup(player)
        screen = pygame.display.set_mode((800, 600))
        self.obj.draw_sprite_color(self.obj,(20,20,100));
        clock = pygame.time.Clock()
        pygame.key.set_repeat(5, 5)


        running = True

        while running:
            screen.fill((20, 10, 10))


            timedelta = clock.tick(30)
            timedelta /= 1000;

            screen.blit(self.obj.update(self.obj),(100,0))
            screen.blit(player.update(player,timedelta), (player.get_position(player)))
            player.collider_enter(player,self.obj)
            pygame.display.flip()



WindowFrame.update(WindowFrame)


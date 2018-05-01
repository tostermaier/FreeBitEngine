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

        screen = pygame.display.set_mode((800, 600))

        clock = pygame.time.Clock()
        pygame.key.set_repeat(5, 5)


        running = True

        while running:
            screen.fill((20, 10, 10))


            timedelta = clock.tick(30)
            timedelta /= 1000;

            screen.blit(self.obj.move_object(self.obj, 20, 20), (0, self.obj.get_pos_x(self.obj)))
            screen.blit(player.update(player,timedelta), (player.get_pos_x(player), player.get_pos_y(player)))
            pygame.display.flip()



WindowFrame.update(WindowFrame)


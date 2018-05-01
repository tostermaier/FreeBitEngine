import pygame
from engine.graphic import Sprite
from engine.game import GameObject
from engine.game import Player

player = Player.Player
class WindowFrame:
    sprite = Sprite.Sprite()
    obj = GameObject.GameObject


    def update(self):
        pygame.init()

        screen = pygame.display.set_mode((800, 600))

        clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 1)


        running = True
        screen.fill((20, 10, 10))
        x = 0
        while running:
            pygame.display.update()
            player.input(player)



            screen.blit(self.obj.move_object(self.obj, 20, 20), (0, self.obj.get_pos_x(self.obj)))
            screen.blit(player.move_object(player, player.get_pos_x(player), player.get_pos_y(player)), (player.get_pos_x(player), player.get_pos_y(player)))
            pygame.display.flip()


            clock.tick(30)


WindowFrame.update(WindowFrame)


from engine.game.GameObject import GameObject
import pygame


class Player(GameObject):

    def __init__(self):
        pass


    def input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_w]:

                    self.set_pos_x(self,self.get_pos_x(self)+10)
                    print(self.get_pos_x(self))
                    self.set_pos_x(self, self.get_pos_x(self) + 10)
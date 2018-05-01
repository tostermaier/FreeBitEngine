import pygame


class InputEvent:
    def __init__(self):
        pass

    def input(self):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:

                    if pygame.key.get_pressed()[pygame.K_w]:
                        if pygame.key.get_pressed()[pygame.K_SPACE]:
                            self.set_shoot(True)
                        self.move_vertical(-5)
                    if pygame.key.get_pressed()[pygame.K_s]:
                        if pygame.key.get_pressed()[pygame.K_SPACE]:
                            self.set_shoot(True)
                        self.move_vertical(5)

                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        self.set_shoot(True)
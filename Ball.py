import pygame
from random import randint
# colours
black = (0, 0, 0)

class Ball(pygame.sprite.Sprite):

    # Call sprite constructor
    def __init__(self, colour, width, height):
        super().__init__()
        # set colour, width and height
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw ball
        pygame.draw.rect(self.image, colour, [0, 0, width, height])
        Vx = randint(4, 9)
        Vy = randint(1, 3)
        self.velocity = [Vx, Vy]
        # Get image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        if self.velocity[1] > 0:
            self.velocity[1] = randint(-6, -4)
        else:
            self.velocity[1] = randint(2, 5)

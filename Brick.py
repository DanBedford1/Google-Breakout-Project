import pygame
# colours
black = (0, 0, 0)

class Brick(pygame.sprite.Sprite):
    # Call constructor
    def __init__(self, colour, width, height):
        super().__init__()

        # Pass colour, width, and height
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw the brick
        pygame.draw.rect(self.image, colour, [0, 0, width, height])

        # Fetch image
        self.rect = self.image.get_rect()

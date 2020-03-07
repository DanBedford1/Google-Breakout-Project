import pygame
# colours
black = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self, colour, width, height):
        # Call sprite constructor
        super().__init__()

        # Pass paddle attributes
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Draw paddle
        pygame.draw.rect(self.image, colour, [0, 0, width, height])
        # Get image
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels
        # Check paddle is on screen
        if self.rect.x > 700:
            self.rect.x = 700

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # Check paddle is on screen
        if self.rect.x < 0:
            self.rect.x = 0



import pygame
from UserPaddle import Paddle
from Ball import Ball
from Brick import Brick
from random import randint
pygame.init()

# Defining colours to use
black = (0, 0, 0)
white = (255, 255, 255)
darkBlue = (36, 90, 190)
lightBlue = (0, 176, 240)
red = (255, 0, 0)
orange = (255, 100, 0)
yellow = (255, 255, 0)
grey = (80, 80, 80)
purple = (140, 117, 223)
green = (0, 0, 255)
colours = ["", white, darkBlue, lightBlue, red, orange, yellow, purple, green]
# set score and lives
score = 0
lives = 5

# Open window
size = (810, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Google Breakout Game")

# Create sprite list
all_sprites = pygame.sprite.Group()
# Instantiate a paddle
paddle = Paddle(orange, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# Instantiate a ball
ball = Ball(red, 10, 10)
ball.rect.x = 300
ball.rect.y = 400

all_bricks = pygame.sprite.Group()
for j in range(1, 9):
    for i in range(10):
        brick = Brick(colours[j], 80, 30)
        brick.rect.x = i * 81
        brick.rect.y = j * 40
        all_sprites.add(brick)
        all_bricks.add(brick)

all_sprites.add(paddle)
all_sprites.add(ball)

Playing = True
clock = pygame.time.Clock()

# Main Game loop
while Playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Playing = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        paddle.moveLeft(10)
    if key[pygame.K_RIGHT]:
        paddle.moveRight(10)

    all_sprites.update()

    # Check for ball bounce
    wall_sound = pygame.mixer.Sound("ping_pong_8bit_plop_1.wav")
    if ball.rect.x >= 800:
        ball.velocity[0] = -ball.velocity[0]
        wall_sound.play()
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
        wall_sound.play()
    if ball.rect.y > 590:
        lives -= 1
        ball.velocity[1] = -ball.velocity[1]
        pygame.mixer.Sound("pacman_death.wav").play()
        pygame.time.wait(1500)
        ball.rect.x = 300
        ball.rect.y = 400
        ball.velocity[0] = randint(4, 9)
        ball.velocity[1] = randint(1, 3)
        if lives == 0:
            # Show END OF GAME message
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER! Score: " + str(score), 1, black)
            screen.blit(text, (100, 250))
            pygame.display.flip()
            pygame.time.wait(5000)
            Playing = False
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]
        wall_sound.play()

    # Collision detection for ball and paddle
    if pygame.sprite.collide_mask(paddle, ball):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        bounce_sound = pygame.mixer.Sound("ping_pong_8bit_beeep.wav")
        bounce_sound.play()
        ball.bounce()

    # Collision detection for ball and brick
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        break_sound = pygame.mixer.Sound("Explosion+1.wav")
        break_sound.play()
        brick.kill()
        if len(all_bricks) == 0:
            # Display GAME WON message
            font = pygame.font.Font(None, 74)
            text = font.render("GAME WON!!", 1, white)
            screen.blit(text, (100, 250))
            pygame.display.flip()
            pygame.time.wait(5000)

            # Stop the Game
            Playing = False

    # Clearing Screen
    screen.fill(grey)
    pygame.draw.line(screen, black, [0, 38], [800, 38], 2)

    # Showing lives and score
    font = pygame.font.Font(None, 30)
    text = font.render("Score: " + str(score), 1, white)
    screen.blit(text, (20, 10))
    text = font.render("Lives: " + str(lives), 1, white)
    screen.blit(text, (500, 10))

    # Draw sprites
    all_sprites.draw(screen)

    # Update screen and set frame rate to 60
    pygame.display.flip()
    clock.tick(60)

# Quit game upon exit of main loop
pygame.quit()

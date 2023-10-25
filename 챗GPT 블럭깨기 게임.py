#pip install pygame
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BRICK_WIDTH = 100
BRICK_HEIGHT = 30
BRICK_ROWS = 4
BRICK_COLS = 6

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# Ball properties
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT - 20, 30, 30)
ball_speed_x, ball_speed_y = BALL_SPEED, -BALL_SPEED

# Paddle properties
paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 10, 120, 10)

# Brick properties
bricks = []
brick_color = [WHITE, RED]
for row in range(BRICK_ROWS):
    for col in range(BRICK_COLS):
        brick = pygame.Rect(
            col * (BRICK_WIDTH + 5) + 50,
            row * (BRICK_HEIGHT + 5) + 50,
            BRICK_WIDTH,
            BRICK_HEIGHT,
        )
        bricks.append(brick)

# Initialize the score
score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle.x += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # Paddle collision
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y

    # Brick collisions
    for brick in bricks:
        if ball.colliderect(brick):
            ball_speed_y = -ball_speed_y
            bricks.remove(brick)
            score += 10

    # Clear the screen
    screen.fill(BLACK)

    # Draw the bricks
    for brick in bricks:
        pygame.draw.rect(screen, brick_color[0], brick)

    # Draw the paddle
    pygame.draw.rect(screen, WHITE, paddle)

    # Draw the ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # Display the score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (20, 20))

    pygame.display.update()

    # Game over condition
    if ball.top > HEIGHT:
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, WHITE)
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

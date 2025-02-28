import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fireplanes Fighting Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Plane settings
plane_width, plane_height = 50, 40
plane_x, plane_y = WIDTH // 2, HEIGHT // 2
plane_speed = 5

# Player 2 settings
plane2_x, plane2_y = WIDTH // 4, HEIGHT // 4

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Get keys pressed for Player 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        plane_x -= plane_speed
    if keys[pygame.K_RIGHT]:
        plane_x += plane_speed
    if keys[pygame.K_UP]:
        plane_y -= plane_speed
    if keys[pygame.K_DOWN]:
        plane_y += plane_speed

    # Get keys pressed for Player 2
    if keys[pygame.K_a]:
        plane2_x -= plane_speed
    if keys[pygame.K_d]:
        plane2_x += plane_speed
    if keys[pygame.K_w]:
        plane2_y -= plane_speed
    if keys[pygame.K_s]:
        plane2_y += plane_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        plane_x -= plane_speed
    if keys[pygame.K_RIGHT]:
        plane_x += plane_speed
    if keys[pygame.K_UP]:
        plane_y -= plane_speed
    if keys[pygame.K_DOWN]:
        plane_y += plane_speed

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the planes
    pygame.draw.rect(screen, BLUE, (plane_x, plane_y, plane_width, plane_height))
    pygame.draw.rect(screen, (255, 0, 0), (plane2_x, plane2_y, plane_width, plane_height))  # Player 2 in red


    # Update the display
    pygame.display.flip()

    # Frame rate

    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(60)


import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path/to/your/image.png')
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Adjust scale as needed
picture = pygame.transform.scale(picture, scale)

# Create a rectangle for the picture
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)  # Center on the screen

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    main_surface.fill((0, 0, 0))  # Black background

    # Blit the picture at the centered position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

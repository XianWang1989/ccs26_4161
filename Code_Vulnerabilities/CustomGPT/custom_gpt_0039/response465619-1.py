
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
image = pygame.image.load('path/to/your/image.png')
image_rect = image.get_rect()

# Get the scaled size (replace `aspect_scale` with your function)
scale = aspect_scale(image_rect.size)
image = pygame.transform.scale(image, scale)

# Center the image
image_rect.center = main_surface.get_rect().center

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black (or any color)
    main_surface.fill((0, 0, 0))

    # Blit the image at the centered position
    main_surface.blit(image, image_rect)

    # Update the display
    pygame.display.update()

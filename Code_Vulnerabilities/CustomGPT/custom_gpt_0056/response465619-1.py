
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path/to/your/image.png')  # Update with your image path
size = picture.get_size()

# Scale the image if needed (optional)
def aspect_scale(size, scale_factor=1):
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the image
picture_rect = picture.get_rect()

# Center the image on the screen
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the main surface with white (or any other color)
    main_surface.fill((255, 255, 255))

    # Draw the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

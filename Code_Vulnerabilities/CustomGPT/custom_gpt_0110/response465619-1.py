
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path/to/your/image.png'
picture = pygame.image.load(image_path)

# Scale the image while maintaining aspect ratio (assuming aspect_scale is defined)
def aspect_scale(size):
    # Define your scaling logic here
    return (size[0] // 2, size[1] // 2)  # Example: scale down to half

size = picture.get_size()
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rect of the scaled image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black (or any color)
    main_surface.fill((0, 0, 0))

    # Blit the image to the center
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

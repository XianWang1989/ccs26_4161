
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path/to/your/image.png')

# Scale the image if needed
def aspect_scale(size, scale_factor=1):
    width, height = size
    return (int(width * scale_factor), int(height * scale_factor))

# Get the scaled size
size = picture.get_size()
scale = aspect_scale(size, 1)  # Adjust the scale factor as needed
picture = pygame.transform.scale(picture, scale)

# Create a rectangle for the image and center it
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any color

    # Blit the image at the center of the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

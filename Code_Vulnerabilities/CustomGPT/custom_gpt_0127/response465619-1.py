
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image if needed
def aspect_scale(size):
    # Example scaling function; modify as necessary
    new_width = size[0] // 2  # Scale down to half for demonstration
    new_height = size[1] // 2
    return (new_width, new_height)

# Prepare the image
size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    main_surface.fill((255, 255, 255))  # White background

    # Blit the image at the calculated position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

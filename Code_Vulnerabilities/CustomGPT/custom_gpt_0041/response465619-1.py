
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
image_path = "your_image.png"  # Replace with your image path
picture = pygame.image.load(image_path)

# Optionally scale the image if necessary
def aspect_scale(size):
    # Example scaling function, modify as needed
    return (int(size[0] / 2), int(size[1] / 2))  # Just an example

# Get the scaled size
size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the image
picture_rect = picture.get_rect(center = (screen_size[0] // 2, screen_size[1] // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background (optional)
    main_surface.fill((0, 0, 0))  # Fill with black

    # Blit the image centered on the surface
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

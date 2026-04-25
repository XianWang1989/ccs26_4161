
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path_to_your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale image (optional)
def aspect_scale(size):
    # Assuming you want to maintain aspect ratio, define your scale logic here
    return (size[0] // 2, size[1] // 2)

size = picture.get_size()
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Create a rect for the image and set its center to the center of the screen
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the main surface with a color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the image onto the surface
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

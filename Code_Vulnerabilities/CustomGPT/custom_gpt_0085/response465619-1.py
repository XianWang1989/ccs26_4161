
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path_to_your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image if needed
def aspect_scale(size, max_size=(2560, 1440)):
    # Example scaling function
    width, height = size
    scale_factor = min(max_size[0] / width, max_size[1] / height)
    return (int(width * scale_factor), int(height * scale_factor))

size = picture.get_size()
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rect of the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))

    # Blit the picture at the centered position
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

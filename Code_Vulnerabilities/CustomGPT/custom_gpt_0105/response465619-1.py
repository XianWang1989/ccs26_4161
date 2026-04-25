
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path_to_your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image if needed (optional)
def aspect_scale(size, max_height=1440):
    aspect_ratio = size[0] / size[1]
    new_height = max_height
    new_width = int(new_height * aspect_ratio)
    return new_width, new_height

size = picture.get_size()
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rectangle for positioning
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((255, 255, 255))  # Fill with white background

    # Blit the image at the centered position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

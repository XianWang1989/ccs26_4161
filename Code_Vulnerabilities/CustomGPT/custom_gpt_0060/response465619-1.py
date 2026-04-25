
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = "path_to_your_image.png"  # Update with your image path
picture = pygame.image.load(image_path)

# Optionally, scale the image
def aspect_scale(size, target_width, target_height):
    width, height = size
    if width > target_width or height > target_height:
        scale_factor = min(target_width / width, target_height / height)
        return (int(width * scale_factor), int(height * scale_factor))
    return size

# Scale the image to maintain aspect ratio
scaled_size = aspect_scale(picture.get_size(), screen_width, screen_height)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rectangle of the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    main_surface.fill((0, 0, 0))

    # Draw the image in the center of the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

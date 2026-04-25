
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path/to/your/image.png'  # Update this with your image path
picture = pygame.image.load(image_path)

# Scale the image to maintain aspect ratio (optional)
def aspect_scale(size, max_width, max_height):
    width, height = size
    scale_ratio = min(max_width / width, max_height / height)
    return (int(width * scale_ratio), int(height * scale_ratio))

# Set desired max dimensions
max_width, max_height = 2560, 1440
scaled_size = aspect_scale(picture.get_size(), max_width, max_height)
picture = pygame.transform.scale(picture, scaled_size)

# Create picture rect and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the picture onto the main surface
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

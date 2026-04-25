
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load image
image_path = "path/to/your/image.png"  # Update with your image path
picture = pygame.image.load(image_path)

# Scale image while maintaining aspect ratio
def aspect_scale(size, target_size):
    aspect_ratio = size[0] / size[1]
    if aspect_ratio > 1:  # Wider than tall
        new_size = (target_size[0], int(target_size[0] / aspect_ratio))
    else:  # Taller than wide
        new_size = (int(target_size[1] * aspect_ratio), target_size[1])
    return new_size

# Get original size and scale
size = picture.get_size()
scale = aspect_scale(size, (2560, 1440))
picture = pygame.transform.scale(picture, scale)

# Get the rectangle for positioning
picture_rect = picture.get_rect(center=main_surface.get_rect().center)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((0, 0, 0))  # Optional: Set background color

    # Blit the picture to the center
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Clean up
pygame.quit()
sys.exit()

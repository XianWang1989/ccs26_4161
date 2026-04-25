
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load image
image_path = 'path_to_your_image.png'
picture = pygame.image.load(image_path)

# Scale the image (optional)
def aspect_scale(size, target_width):
    aspect_ratio = size[0] / size[1]
    height = int(target_width / aspect_ratio)
    return (target_width, height)

target_size = 800  # Example target width for scaling
scaled_size = aspect_scale(picture.get_size(), target_size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rectangle for the scaled image
picture_rect = picture.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    main_surface.fill((0, 0, 0))

    # Blit the image at the center
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

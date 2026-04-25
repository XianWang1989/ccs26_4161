
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path/to/your/image.png'  # Update the path to your image
picture = pygame.image.load(image_path)

# Scale the image (if needed)
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling
picture = pygame.transform.scale(picture, scale)

# Get the rect of the scaled image
picture_rect = picture.get_rect()
# Center the image rect in the main surface
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the image centered on the main surface
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

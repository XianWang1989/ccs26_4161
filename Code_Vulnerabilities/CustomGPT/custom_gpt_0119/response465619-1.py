
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale your image
picture = pygame.image.load("path/to/your/image.png")  # Replace with your image path
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Change scale factor as needed
picture = pygame.transform.scale(picture, scale)

# Get the rect for the image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the picture onto the surface at the rect's position
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

pygame.quit()
sys.exit()


import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
image = pygame.image.load('path/to/your/image.png')
size = image.get_size()
# Assuming aspect_scale is a function defined elsewhere
scale = aspect_scale(size)  
image = pygame.transform.scale(image, scale)

# Get the rectangular area of the image
image_rect = image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)  # Center the image

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Draw the image at the center
    main_surface.blit(image, image_rect)

    # Update the display
    pygame.display.update()

pygame.quit()
sys.exit()

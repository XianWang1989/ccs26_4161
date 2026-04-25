
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load("path/to/your/image.png")
size = picture.get_size()

# Function to scale the image while maintaining aspect ratio
def aspect_scale(size, max_width=2560, max_height=1440):
    scale = min(max_width / size[0], max_height / size[1])
    return (int(size[0] * scale), int(size[1] * scale))

# Scale the image
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rectangle for the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black (or any background color)
    main_surface.fill((0, 0, 0))

    # Blit the image centered on the surface
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()

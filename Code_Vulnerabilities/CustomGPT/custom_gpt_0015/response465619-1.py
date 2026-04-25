
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path/to/your/image.png')
size = picture.get_size()

# Scale the image if needed
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling factor
picture = pygame.transform.scale(picture, scale)

# Get the rectangle for positioning
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the picture onto the surface
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()


import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions and create the main surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
picture = pygame.image.load('path/to/your/image.png')  # Update with your image path

# Get the scaled size and scale
size = picture.get_size()
scale = (int(size[0] * aspect_scale(size)), int(size[1] * aspect_scale(size)))
picture = pygame.transform.scale(picture, scale)

# Get the rect of the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((0, 0, 0))  # Black background

    # Blit the image at the rect's coordinates
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

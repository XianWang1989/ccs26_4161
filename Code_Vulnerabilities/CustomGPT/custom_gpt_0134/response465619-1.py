
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = "path/to/your/image.png"  # Update with your image path
picture = pygame.image.load(image_path)

# Scale the image if necessary
size = picture.get_size()
scale = aspect_scale(size)  # Ensure you define this function properly
picture = pygame.transform.scale(picture, (scale))

# Get the center rect
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((0, 0, 0))  # Fill with black

    # Blit the image on the main surface
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

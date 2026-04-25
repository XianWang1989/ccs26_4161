
import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale image
image_path = "path_to_image.png"  # Replace with your image path
picture = pygame.image.load(image_path)
size = picture.get_size()

# Scaling function if needed
def aspect_scale(size):
    # Example scaling; adapt to your needs
    scale_factor = 0.5  # Adjust scale as necessary
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Calculate center position
picture_rect = picture.get_rect(center=(screen_width / 2, screen_height / 2))

# Main loop (simplified)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    main_surface.fill((0, 0, 0))  # Fill with black or desired color
    # Blit the centered image
    main_surface.blit(picture, picture_rect.topleft)
    pygame.display.update()

pygame.quit()

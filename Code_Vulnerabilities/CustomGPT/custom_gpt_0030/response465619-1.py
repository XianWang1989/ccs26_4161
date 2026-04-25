
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path_to_your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)
size = picture.get_size()

# Scale the image if needed (function to determine scale can be defined)
def aspect_scale(size):
    scale_factor = 0.5  # Example scale factor
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the scaled image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((0, 0, 0))  # Black background

    # Blit the image centered on the screen
    main_surface.blit(picture, picture_rect.topleft)  # Use topleft because picture_rect is already centered

    # Update the display
    pygame.display.update()

pygame.quit()

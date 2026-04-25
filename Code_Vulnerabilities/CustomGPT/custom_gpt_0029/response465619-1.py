
import pygame

# Initialize Pygame
pygame.init()

# Set up the main surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path_to_your_image.png')
size = picture.get_size()

# Scale the image as needed (this is an example scaling function)
def aspect_scale(size):
    scale_factor = 0.5  # Adjust scaling as needed
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

# Scale the image
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rect for positioning
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((0, 0, 0))  # Black background

    # Blit the centered image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

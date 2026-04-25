
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path_to_your_image.png')
size = picture.get_size()

# Scale the image if necessary (optional)
scale = aspect_scale(size)  # Implement aspect_scale according to your needs
picture = pygame.transform.scale(picture, (scale))

# Get the rect of the scaled picture
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))

    # Blit the image centered on the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

pygame.quit()

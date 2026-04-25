
import pygame

# Initialize Pygame
pygame.init()

# Set up the main surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load(images[i])
size = picture.get_size()

# Scale the image if needed (implement aspect_scale accordingly)
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, (scale))

# Get the rect for the picture and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background (optional)
    main_surface.fill((255, 255, 255))

    # Draw the scaled picture centered on the main surface
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

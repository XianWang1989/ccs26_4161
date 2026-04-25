
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
main_surface = pygame.display.set_mode((2560, 1440))

# Load the image
picture = pygame.image.load(images[i])
size = picture.get_size()
scale = aspect_scale(size)  # Assuming this function is defined elsewhere
picture = pygame.transform.scale(picture, (scale))

# Get the image's rect and center it
picture_rect = picture.get_rect(center=(2560 // 2, 1440 // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((0, 0, 0))

    # Blit the picture at its centered position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

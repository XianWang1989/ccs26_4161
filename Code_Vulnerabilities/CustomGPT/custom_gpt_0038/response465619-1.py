
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
picture = pygame.image.load(images[i])
size = picture.get_size()
scale = aspect_scale(size)  # Assuming you've defined aspect_scale elsewhere
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the image
picture_rect = picture.get_rect()

# Center the image on the main surface
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background (optional)
    main_surface.fill((0, 0, 0))  # Black background

    # Blit the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

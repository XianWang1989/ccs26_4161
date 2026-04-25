
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load(images[i])
size = picture.get_size()

# Scale the image if needed (implement aspect_scale as required)
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rect of the image
picture_rect = picture.get_rect()

# Center the image rect in the main surface
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((0, 0, 0))  # Fill with black or any other color

    # Blit the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

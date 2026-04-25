
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path/to/your/image.png')
size = picture.get_size()
scale = aspect_scale(size)  # Define your aspect_scale function as needed
picture = pygame.transform.scale(picture, scale)

# Get the rect of the image and center it
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((255, 255, 255))  # Fill with white (or any color)

    # Blit the picture onto the main surface at the centered position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

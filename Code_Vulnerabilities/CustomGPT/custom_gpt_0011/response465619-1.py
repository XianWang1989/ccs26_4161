
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
picture = pygame.image.load('path_to_your_image.png')  # Replace with the path to your image
size = picture.get_size()

# Scale the image as needed
scale = aspect_scale(size)  # Define your aspect_scale function as necessary
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the picture and center it
picture_rect = picture.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((255, 255, 255))  # Fill with white or your preferred color

    # Draw the picture on the main surface
    main_surface.blit(picture, picture_rect.topleft)  # Use topleft to position it correctly
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

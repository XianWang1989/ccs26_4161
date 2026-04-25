
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
picture = pygame.image.load('path_to_your_image.png')

# Scale your image if necessary
size = picture.get_size()
scale = aspect_scale(size)  # Define your aspect_scale function accordingly
picture = pygame.transform.scale(picture, (scale))

# Calculate the position to center the image
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any other color

    # Blit the image at the centered position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

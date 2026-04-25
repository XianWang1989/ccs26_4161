
import pygame
import sys

pygame.init()

# Set up the main surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load("your_image.png")  # Replace with your image path
size = picture.get_size()
scale = aspect_scale(size)  # Ensure you have your aspect scale function defined
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the picture
picture_rect = picture.get_rect()

# Calculate position to center the image
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any color you prefer

    # Blit the picture on the center of the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

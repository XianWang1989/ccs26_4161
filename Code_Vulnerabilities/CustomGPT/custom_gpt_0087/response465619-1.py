
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the screen size
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
picture = pygame.image.load('path_to_your_image.png')

# Center the image
picture_rect = picture.get_rect()
picture_rect.center = (screen_size[0] // 2, screen_size[1] // 2)

# Scale the image if necessary
size = picture.get_size()
scale = aspect_scale(size)  # Define your aspect_scale function as needed
picture = pygame.transform.scale(picture, (scale))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))

    # Draw the picture at the centered position
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

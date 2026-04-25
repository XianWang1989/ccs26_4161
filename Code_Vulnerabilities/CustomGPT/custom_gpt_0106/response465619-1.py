
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen size
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
picture = pygame.image.load(images[i])
size = picture.get_size()

# Scale the image using your aspect_scale function
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rect of the image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the surface
    main_surface.fill((0, 0, 0))

    # Draw the image in the center of the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

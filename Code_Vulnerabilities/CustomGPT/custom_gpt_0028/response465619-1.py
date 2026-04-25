
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the main surface (screen) with the given resolution
main_surface = pygame.display.set_mode((2560, 1440))

# Load the image
images = ["path_to_your_image.png"]  # Update with your image path
picture = pygame.image.load(images[0])

# Get the rect of the picture and center it about the main surface
picture_rect = picture.get_rect(center=main_surface.get_rect().center)

# Scale the image if necessary (optional)
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling to 50%
picture = pygame.transform.scale(picture, scale)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a background color (optional)
    main_surface.fill((0, 0, 0))  # Fill with black background

    # Draw the centered image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

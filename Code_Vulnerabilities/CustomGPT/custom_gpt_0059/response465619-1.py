
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the screen size
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
image_path = 'path_to_your_image.png'  # Update with your image path
picture = pygame.image.load(image_path)

# Get the image rect and scale if necessary
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scale by 50%
picture = pygame.transform.scale(picture, scale)

# Get the rectangle for the scaled image
picture_rect = picture.get_rect()

# Center the image in the screen
picture_rect.center = main_surface.get_rect().center

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))

    # Blit the picture onto the main surface
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

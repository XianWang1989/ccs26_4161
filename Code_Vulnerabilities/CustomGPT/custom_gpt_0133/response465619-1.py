
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
picture = pygame.image.load('path_to_your_image.png')  # Replace with your image path
# Get the rect for the image and center it in the middle of the screen
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Scale image (optional)
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling to 50%
picture = pygame.transform.scale(picture, scale)
picture_rect = picture.get_rect(center=picture_rect.center)  # Update the picture rect after scaling

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black
    main_surface.fill((0, 0, 0))

    # Blit the image to the screen at the centered position
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

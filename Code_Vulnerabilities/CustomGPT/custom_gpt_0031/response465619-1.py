
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
picture = pygame.image.load("path_to_your_image.png")
size = picture.get_size()

# Optionally scale the image
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling by 50%
picture = pygame.transform.scale(picture, scale)

# Create a rect for the picture
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))

    # Blit the picture at the center position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

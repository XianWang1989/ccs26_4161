
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
image_path = 'path_to_your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling factor
picture = pygame.transform.scale(picture, scale)

# Create a rectangle for the image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black color

    # Blit the image onto the surface
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

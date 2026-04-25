
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 2560, 1440
main_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Center Image Example')

# Load image
picture = pygame.image.load('path/to/your/image.png')
size = picture.get_size()

# Scale the image if necessary (adjust scale function if needed)
def aspect_scale(size):
    scale_factor = 1  # Replace with your desired scale factor
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)
picture_rect = picture.get_rect(center=(width // 2, height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any color

    # Draw the image centered
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

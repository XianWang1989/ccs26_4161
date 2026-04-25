
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the main surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
picture = pygame.image.load('path/to/your/image.png')

# Scale image if necessary (this function needs to be defined as per your scaling logic)
def aspect_scale(size, target_size=(2560, 1440)):
    # Calculate scaling based on aspect ratio
    scale = min(target_size[0] / size[0], target_size[1] / size[1])
    return (int(size[0] * scale), int(size[1] * scale))

# Get picture details
picture_rect = picture.get_rect()  # Get the rect of the image
scaled_size = aspect_scale(picture.get_size())
picture = pygame.transform.scale(picture, scaled_size)

# Center the image on the screen
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    main_surface.fill((0, 0, 0))

    # Blit the picture
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

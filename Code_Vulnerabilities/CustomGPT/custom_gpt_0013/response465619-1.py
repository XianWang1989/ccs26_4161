
import pygame

# Initialize Pygame
pygame.init()

# Constants for screen size
SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440

# Create the main surface
main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load your image
images = ['path_to_your_image.png']  # Replace with your image path
picture = pygame.image.load(images[0])

# Get the rect of the image
picture_rect = picture.get_rect()

# Scale the image if necessary (modify aspect_scale function as needed)
def aspect_scale(size):
    # Example scaling function
    scale_factor = min(SCREEN_WIDTH / size[0], SCREEN_HEIGHT / size[1])
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

size = picture.get_size()
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Center the image on the screen
picture_rect = picture.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    main_surface.fill((0, 0, 0))

    # Blit the picture at the centered position
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

pygame.quit()

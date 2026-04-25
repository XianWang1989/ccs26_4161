
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set constants
SCREEN_WIDTH, SCREEN_HEIGHT = 2560, 1440
main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def aspect_scale(size):
    # Define your scaling function here if needed
    return size

# Load and scale the image
images = ["your_image.png"]  # Replace with your image path
i = 0
picture = pygame.image.load(images[i])
size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle for the image and set its center to the center of the screen
picture_rect = picture.get_rect()
picture_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

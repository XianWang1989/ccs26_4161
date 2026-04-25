
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = "path/to/your/image.png"  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image if necessary
def aspect_scale(size):
    # Example scaling - adjust as necessary
    scale_width = screen_width // 4  # Scale down to 1/4 of the screen width
    scale_height = int(size[1] * (scale_width / size[0]))
    return (scale_width, scale_height)

size = picture.get_size()
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Create a rectangle for positioning
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))

    # Blit the image centered
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

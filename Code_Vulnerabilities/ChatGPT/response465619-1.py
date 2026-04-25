
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
image_path = "path/to/your/image.png"  # Replace with your image path
picture = pygame.image.load(image_path)

# Function to maintain aspect ratio while scaling
def aspect_scale(size, max_size):
    # Calculate scale factor maintaining aspect ratio
    scale = min(max_size[0] / size[0], max_size[1] / size[1])
    return (int(size[0] * scale), int(size[1] * scale))

# Scale image while maintaining aspect ratio, you can set max_size to your full screen size
scaled_size = aspect_scale(picture.get_size(), (screen_width, screen_height))
picture = pygame.transform.scale(picture, scaled_size)

# Create a rect for the image and center it in the screen
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background (optional)
    main_surface.fill((0, 0, 0))  # Fill with black; set to any color you want

    # Blit the image at the centered position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

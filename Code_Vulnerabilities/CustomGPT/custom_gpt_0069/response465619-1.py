
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = "path/to/your/image.png"
picture = pygame.image.load(image_path)

# Scale the image if necessary (for example purposes)
def aspect_scale(size):
    scale_factor = 1  # Set your scale factor here
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

# Center the image
size = picture.get_size()
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rectangle for positioning
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main_surface.fill((0, 0, 0))  # Fill the screen with black
    main_surface.blit(picture, picture_rect)  # Draw the image
    pygame.display.update()  # Update the display

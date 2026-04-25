
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
image_path = 'your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image if needed
def aspect_scale(size, scale_factor=1):
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

size = picture.get_size()
scale = aspect_scale(size, 1)  # Adjust scale factor as needed
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    main_surface.fill((0, 0, 0))  # Black background

    # Blit the image at the centered position
    main_surface.blit(picture, picture_rect.topleft)  # Use topleft since picture_rect is already centered

    # Update the display
    pygame.display.update()

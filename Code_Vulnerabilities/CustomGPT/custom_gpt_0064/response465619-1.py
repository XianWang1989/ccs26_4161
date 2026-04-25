
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = "path_to_your_image.png"
picture = pygame.image.load(image_path)

# Get picture size and scale (adjust this function based on your needs)
def aspect_scale(size):
    # Example scaling logic
    scale_factor = 0.5  # Change as needed
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

# Scale the image
size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Replace with desired background color

    # Blit the picture to the center of the surface
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

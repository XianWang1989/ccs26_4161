
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
image_path = 'path_to_your_image.png'  # Replace with path to your image
picture = pygame.image.load(image_path)

# Function to scale the image while maintaining aspects
def aspect_scale(size):
    # Calculate scale, for example, you can adjust the size to fit in a predefined area
    scale_factor = 0.5  # Example scale factor
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Scale the image
    size = picture.get_size()
    scale = aspect_scale(size)
    picture = pygame.transform.scale(picture, scale)

    # Get the new rect for the image and center it on the screen
    picture_rect = picture.get_rect(center=main_surface.get_rect().center)

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill the screen with black

    # Blit the image at the corrected position
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

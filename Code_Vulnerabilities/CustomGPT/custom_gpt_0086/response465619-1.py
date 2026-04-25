
import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path/to/your/image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image (optional, based on your needs)
def aspect_scale(size, scale_factor):
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

scale_factor = 1  # Adjust as needed
scaled_size = aspect_scale(picture.get_size(), scale_factor)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rectangle of the image for centering
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((0, 0, 0))  # Fill with black

    # Blit the image at the centered rect position
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()


import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
image_path = 'path_to_your_image.png'
picture = pygame.image.load(image_path)

# Scale the image to maintain aspect ratio (optional)
def aspect_scale(size, scale_factor):
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

# Define scale factor (modify based on your needs)
scale_factor = 0.5  # This is just an example; adjust as needed.
scaled_size = aspect_scale(picture.get_size(), scale_factor)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rect for the image centered on the screen
picture_rect = picture.get_rect(center=(screen_width / 2, screen_height / 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black (or any other background color)
    main_surface.fill((0, 0, 0))

    # Blit the picture onto the main_surface, centered
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

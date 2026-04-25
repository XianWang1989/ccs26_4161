
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load image
image_path = "path/to/your/image.png"  # Update with your image path
picture = pygame.image.load(image_path)

# Scale the image if needed (replace aspect_scale with your scaling logic)
def aspect_scale(size):
    # Example scaling logic, adjust as necessary
    scale_factor = 0.5  # Example scaling factor
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

# Center the image
size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the image and center it on the screen
picture_rect = picture.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    main_surface.fill((0, 0, 0))  # Set background color to black

    # Blit the centered image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

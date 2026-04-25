
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the main surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = "path/to/your/image.png"  # Update with your image path
picture = pygame.image.load(image_path)

# Get image rectangle and scale it if necessary
picture_rect = picture.get_rect()
size = picture.get_size()
scale_factor = 1  # Change this as needed for scaling
scaled_size = (int(size[0] * scale_factor), int(size[1] * scale_factor))
picture = pygame.transform.scale(picture, scaled_size)

# Center the image on the screen
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))

    # Draw the centered image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

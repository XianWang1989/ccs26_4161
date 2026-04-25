
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path_to_your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Get the original image size
original_size = picture.get_size()

# Scaling factor (example: let's say you want to scale it to half its original size)
scale_factor = 0.5
scaled_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))

# Scale the image
picture = pygame.transform.scale(picture, scaled_size)

# Get the new rectangle for the scaled image
picture_rect = picture.get_rect()

# Center the image in the middle of the screen
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color (optional)
    main_surface.fill((255, 255, 255))  # Fill with white for visibility

    # Blit the image at the center
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

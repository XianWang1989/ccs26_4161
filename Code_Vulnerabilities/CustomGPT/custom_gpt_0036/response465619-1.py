
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('your_image_path_here.png')  # Replace with your image path

# Scale the image (optional, adjust based on your scaling logic)
size = picture.get_size()
scale = aspect_scale(size)  # Assuming this function scales your image correctly
picture = pygame.transform.scale(picture, (scale))

# Create a rect for the image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the surface with black or any background color
    main_surface.fill((0, 0, 0))

    # Blit the picture onto the surface at the new rect's position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

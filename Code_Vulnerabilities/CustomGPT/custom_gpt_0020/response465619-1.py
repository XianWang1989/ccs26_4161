
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the main surface/screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = "your_image.png"  # Replace with your image path
picture = pygame.image.load(image_path)

# Function to scale the image maintaining its aspect ratio
def aspect_scale(size, max_size):
    aspect_ratio = float(size[0]) / size[1]
    if size[0] > max_size[0] or size[1] > max_size[1]:
        if aspect_ratio > 1:
            new_width = max_size[0]
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = max_size[1]
            new_width = int(aspect_ratio * new_height)
        return (new_width, new_height)
    return size

# Scale the picture if needed
max_size = (screen_width // 2, screen_height // 2)  # You can set your max size here
scaled_size = aspect_scale(picture.get_size(), max_size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the picture rect and position it in the center of the screen
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((0, 0, 0))  # Fill with black or any color

    # Blit the picture centered
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

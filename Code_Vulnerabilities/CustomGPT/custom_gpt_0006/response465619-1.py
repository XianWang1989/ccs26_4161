
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
image_path = "path/to/your/image.png"  # Replace with your image path
picture = pygame.image.load(image_path)
size = picture.get_size()

# Function to scale the image while maintaining aspect ratio
def aspect_scale(size, max_width, max_height):
    aspect_ratio = size[0] / size[1]
    if size[0] > max_width or size[1] > max_height:
        if aspect_ratio > 1:  # Width is greater than height
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:  # Height is greater than width
            new_height = max_height
            new_width = int(max_height * aspect_ratio)
        return (new_width, new_height)
    return size

# Scale image
scale = aspect_scale(size, screen_width, screen_height)
picture = pygame.transform.scale(picture, scale)

# Center the image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    main_surface.fill((0, 0, 0))

    # Blit the image
    main_surface.blit(picture, picture_rect)

    # Update display
    pygame.display.update()

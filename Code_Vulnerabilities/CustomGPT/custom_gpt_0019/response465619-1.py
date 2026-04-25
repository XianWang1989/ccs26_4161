
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

# Scale the image while maintaining aspect ratio
def aspect_scale(size, target_width, target_height):
    aspect_ratio = size[0] / size[1]
    if target_width / target_height > aspect_ratio:
        return (int(target_height * aspect_ratio), target_height)
    else:
        return (target_width, int(target_width / aspect_ratio))

# Get the appropriate scaled size
size = picture.get_size()
scaled_size = aspect_scale(size, screen_width, screen_height)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rect of the image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white or any color of your choice
    main_surface.fill((255, 255, 255))

    # Blit the picture at the calculated position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

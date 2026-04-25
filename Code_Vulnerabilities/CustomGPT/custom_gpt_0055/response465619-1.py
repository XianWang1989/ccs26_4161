
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
image_path = 'your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image if needed (aspect_scale is not defined here)
def aspect_scale(size, max_width=2560, max_height=1440):
    width, height = size
    scale = min(max_width / width, max_height / height)
    return (int(width * scale), int(height * scale))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the scaled size and center the image
    size = picture.get_size()
    scaled_size = aspect_scale(size)
    picture = pygame.transform.scale(picture, scaled_size)

    # Create a rect for centering
    picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

    # Fill the background and draw the picture
    main_surface.fill((0, 0, 0))  # Fill with black
    main_surface.blit(picture, picture_rect)

    pygame.display.update()

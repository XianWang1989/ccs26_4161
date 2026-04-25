
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the main surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image (adjust this as needed)
def aspect_scale(size, scale_factor=1):
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

# Center the image
def center_image(surface, image):
    size = image.get_size()
    scale = aspect_scale(size)  # Scale factor if needed
    picture_scaled = pygame.transform.scale(image, scale)
    picture_rect = picture_scaled.get_rect(center=surface.get_rect(center=(screen_width // 2, screen_height // 2)).center)
    return picture_scaled, picture_rect

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main_surface.fill((0, 0, 0))  # Clear the screen with black
    picture_scaled, picture_rect = center_image(main_surface, picture)
    main_surface.blit(picture_scaled, picture_rect)
    pygame.display.update()

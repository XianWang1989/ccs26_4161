
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'your_image.png'  # Replace with your image file
picture = pygame.image.load(image_path)

# Function to scale the image while maintaining the aspect ratio
def aspect_scale(size, max_width=2560, max_height=1440):
    width, height = size
    scale = min(max_width / width, max_height / height)
    return int(width * scale), int(height * scale)

# Scale the image
size = picture.get_size()
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rectangle of the image and center it on the screen
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))

    # Blit the image to the center of the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()


import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
image_path = 'path_to_your_image.png'  # Replace this with your image path
picture = pygame.image.load(image_path)

# Scale the image if needed
def aspect_scale(size):
    # Scaling logic goes here
    # For demo purposes, we'll return the original size
    return size

size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((255, 255, 255))  # Fill with white background

    # Blit the image in the center of the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

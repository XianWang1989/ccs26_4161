
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 2560
screen_height = 1440
screen = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = "path_to_your_image.png"  # Replace with your image path
picture = pygame.image.load(image_path)

# Function to scale the image while maintaining aspect ratio
def aspect_scale(size):
    base_width = 800  # Define your desired width
    ratio = base_width / float(size[0])
    return (base_width, int(float(size[1]) * ratio))

# Scale the image
original_size = picture.get_size()
scaled_size = aspect_scale(original_size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rectangle of the image for centering
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (optional)
    screen.fill((255, 255, 255))  # Fill with white

    # Blit the image to the screen at the center position
    screen.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

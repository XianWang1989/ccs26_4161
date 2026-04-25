
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path/to/your/image.png'  # Change this to your image path
picture = pygame.image.load(image_path)

# Scale the image (if needed)
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling to 50%
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the scaled image
picture_rect = picture.get_rect()

# Center the rectangle in the middle of the screen
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any color

    # Draw the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

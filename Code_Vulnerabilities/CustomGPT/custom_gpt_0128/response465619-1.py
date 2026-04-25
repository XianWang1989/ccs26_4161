
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('your_image.png')  # Replace with your image path
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Scale if needed
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any color

    # Blit the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

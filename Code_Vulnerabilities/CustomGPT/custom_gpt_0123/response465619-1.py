
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path/to/your/image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image if necessary
scale = (int(picture.get_width() * 0.5), int(picture.get_height() * 0.5))  # Example scaling by 50%
picture = pygame.transform.scale(picture, scale)

# Get the rect of the image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    main_surface.fill((255, 255, 255))  # Fill with white

    # Blit the image at the centered rect
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

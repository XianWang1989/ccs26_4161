
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('your_image_path.png')  # Replace with your image path
size = picture.get_size()

# Scale the image if necessary (implement aspect_scale as needed)
scale = aspect_scale(size)  # Placeholder for your scaling function
picture = pygame.transform.scale(picture, scale)

# Get the rect of the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))  # Fill with white

    # Blit the image at the centered position
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

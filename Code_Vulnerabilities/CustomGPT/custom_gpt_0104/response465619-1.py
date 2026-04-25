
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
image_path = 'your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image as necessary (optional)
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scale (adjust as needed)
picture = pygame.transform.scale(picture, scale)

# Get the rect of the image
picture_rect = picture.get_rect()

# Center the rect on the main surface
picture_rect.center = main_surface.get_rect().center

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))  # Fill with white background

    # Blit the picture
    main_surface.blit(picture, picture_rect)  # Use picture_rect for correct centering

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

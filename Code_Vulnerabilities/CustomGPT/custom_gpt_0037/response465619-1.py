
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
image_path = "your_image.png"  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image (optional)
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling to 50%
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the scaled image at the center
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

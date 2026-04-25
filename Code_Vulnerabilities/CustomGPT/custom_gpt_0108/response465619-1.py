
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
image_path = 'your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale your image if needed
size = picture.get_size()
scale_factor = 0.5  # Change scale factor as needed
scaled_size = (int(size[0] * scale_factor), int(size[1] * scale_factor))
picture = pygame.transform.scale(picture, scaled_size)

# Get the rectangle of the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the image to the center
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

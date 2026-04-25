
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the screen size
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
picture = pygame.image.load("your_image.png")  # Replace with your image path

# Get the image's rect and scale it if needed
scale_factor = 1  # Adjust this as needed for scaling
size = picture.get_size()
scaled_size = (int(size[0] * scale_factor), int(size[1] * scale_factor))
picture = pygame.transform.scale(picture, scaled_size)
picture_rect = picture.get_rect()

# Center the image on the screen
picture_rect.center = main_surface.get_rect().center

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    main_surface.fill((0, 0, 0))  # Black background or any color you prefer

    # Draw the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

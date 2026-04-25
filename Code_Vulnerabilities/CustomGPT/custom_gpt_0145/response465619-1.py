
import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path_to_your_image.png')  # Replace with your image path

# Get the size of the image
size = picture.get_size()

# Center the image
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Optionally scale the image if needed
scale = aspect_scale(size)  # You might need to define aspect_scale function if you want to scale
picture = pygame.transform.scale(picture, (scale))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any other color

    # Blit the image at the calculated position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

pygame.quit()


import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path_to_image.png')
size = picture.get_size()

# Scale the image if necessary
scale = aspect_scale(size)  # Define this function based on your scaling logic
picture = pygame.transform.scale(picture, (scale))

# Get the rect for the scaled image
picture_rect = picture.get_rect()

# Center the image
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((0, 0, 0))  # Black background

    # Blit the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

pygame.quit()

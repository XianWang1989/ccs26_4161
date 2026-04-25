
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
picture = pygame.image.load('path_to_your_image.png')
size = picture.get_size()

# Scale the image if necessary (assuming aspect_scale is defined elsewhere)
scale = aspect_scale(size)  # Adjust according to your scaling logic
picture = pygame.transform.scale(picture, scale)

# Calculate the rect for the scaled image
picture_rect = picture.get_rect()
picture_rect.center = main_surface.get_rect().center  # Center the image rect

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((0, 0, 0))  # Black background

    # Draw the centered image
    main_surface.blit(picture, picture_rect.topleft)  # Use the top-left corner for blitting

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

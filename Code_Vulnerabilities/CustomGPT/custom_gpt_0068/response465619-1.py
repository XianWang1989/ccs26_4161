
import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
picture = pygame.image.load('your_image.png')  # Replace with your image path

# Scale the image while maintaining aspect ratio
def aspect_scale(size):
    # Implement your scaling logic here
    # For demonstration, we'll return the original size
    return size

# Get the initial size and scale the image
size = picture.get_size()
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the scaled image's rectangle
picture_rect = picture.get_rect()

# Center the image rectangle on the screen
picture_rect.center = main_surface.get_rect().center

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background (optional)
    main_surface.fill((255, 255, 255))  # Fill with white

    # Blit the image
    main_surface.blit(picture, picture_rect.topleft)  # Use top-left position

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

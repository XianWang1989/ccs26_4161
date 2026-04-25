
import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load(images[i])
size = picture.get_size()

# Scale the image (adjust the aspect_scale function as needed)
scale = aspect_scale(size)  # Assume aspect_scale returns the correct scale tuple
picture = pygame.transform.scale(picture, scale)

# Create a rect for the scaled picture
picture_rect = picture.get_rect()

# Center the rect on the screen
picture_rect.center = main_surface.get_rect().center

# Main loop (to keep the window open)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any background color

    # Blit the picture at the centered position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

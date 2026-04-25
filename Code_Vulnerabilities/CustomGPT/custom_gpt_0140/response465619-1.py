
import pygame

# Initialize Pygame
pygame.init()

# Set up screen size
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
picture = pygame.image.load(images[i])

# Scale the image if necessary
size = picture.get_size()
scale = aspect_scale(size)  # Make sure aspect_scale() is defined
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the picture
picture_rect = picture.get_rect()

# Center the rectangle in the middle of the screen
picture_rect.center = main_surface.get_rect().center

# Clear the screen (optional)
main_surface.fill((0, 0, 0))

# Blit the image
main_surface.blit(picture, picture_rect.topleft)

# Update the display
pygame.display.update()

# Main loop (for the window to remain open)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

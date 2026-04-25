
import pygame

# Initialize Pygame
pygame.init()

# Set up the main surface (window)
main_surface = pygame.display.set_mode((2560, 1440))

# Load your image
picture = pygame.image.load(images[i])

# Get the image rectangle
picture_rect = picture.get_rect()

# Scale the image if needed
size = picture.get_size()
scale = aspect_scale(size)  # Assuming you have this function defined
picture = pygame.transform.scale(picture, (scale))

# Center the rectangle (this centers the rectangle itself, not the image's top-left corner)
picture_rect.center = main_surface.get_rect().center

# Blit the image, using the top-left corner of the rectangle
main_surface.blit(picture, picture_rect.topleft)  # Use topleft for blitting

# Update the display
pygame.display.update()

# Main loop (for illustration)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

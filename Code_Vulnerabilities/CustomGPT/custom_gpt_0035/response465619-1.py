
import pygame

# Initialize Pygame
pygame.init()

# Set up the main surface
main_surface = pygame.display.set_mode((2560, 1440))

# Load and scale the image
picture = pygame.image.load(images[i])
size = picture.get_size()
scale = aspect_scale(size)  # Ensure aspect_scale is defined for scaling
picture = pygame.transform.scale(picture, (scale))

# Get rectangle and center it
picture_rect = picture.get_rect()
picture_rect.center = main_surface.get_rect().center

# Blit the picture at the center of the screen
main_surface.blit(picture, picture_rect.topleft)

# Update the display
pygame.display.update()

# Main loop (add your logic to exit the loop properly)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

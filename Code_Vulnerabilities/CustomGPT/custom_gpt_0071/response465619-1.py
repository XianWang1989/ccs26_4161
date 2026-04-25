
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
picture = pygame.image.load(images[i])
size = picture.get_size()

# Scale the image (assuming `aspect_scale` is defined)
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, (scale))

# Get the image rect and set its center
picture_rect = picture.get_rect()
picture_rect.center = (screen_size[0] // 2, screen_size[1] // 2)

# Blit the image onto the main surface
main_surface.blit(picture, picture_rect.topleft)

# Update the display
pygame.display.update()

# Event loop (for window management)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

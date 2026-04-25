
import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load(images[i])

# Scale the image (assuming aspect_scale is defined)
size = picture.get_size()
scale = aspect_scale(size)  # Ensure this returns a tuple (new_width, new_height)
picture = pygame.transform.scale(picture, scale)

# Get the rect of the scaled picture
picture_rect = picture.get_rect()

# Center the picture in the middle of the screen
picture_rect.center = (screen_width // 2, screen_height // 2)

# Blit the image on the surface
main_surface.blit(picture, picture_rect)

# Update the display
pygame.display.update()

# Main loop (for example)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

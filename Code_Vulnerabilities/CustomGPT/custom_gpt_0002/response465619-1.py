
import pygame

# Initialize Pygame
pygame.init()

# Set up the main surface
main_surface = pygame.display.set_mode((2560, 1440))

# Load your image
picture = pygame.image.load(images[i])
size = picture.get_size()
scale = aspect_scale(size)  # Scale if necessary
picture = pygame.transform.scale(picture, (scale))

# Get the rect of the image and center it
picture_rect = picture.get_rect(center=(1280, 720))  # Center for 2560x1440

# Blit the image on the main surface
main_surface.blit(picture, picture_rect.topleft)

# Update the display
pygame.display.update()

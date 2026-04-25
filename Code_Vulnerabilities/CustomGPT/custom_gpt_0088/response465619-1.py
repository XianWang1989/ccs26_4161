
import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
picture = pygame.image.load(images[i])
size = picture.get_size()
scale = aspect_scale(size)  # Ensure this function returns the appropriate scaling
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the scaled image
picture_rect = picture.get_rect()

# Center the rectangle in the main surface
picture_rect.center = (screen_width // 2, screen_height // 2)

# Blit the image on the surface
main_surface.blit(picture, picture_rect)

# Update the display
pygame.display.update()

# Don't forget to handle the game loop and quitting

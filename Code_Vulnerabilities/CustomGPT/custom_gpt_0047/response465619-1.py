
import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load("path/to/your/image.png")

# Get the rect of the image and the screen
picture_rect = picture.get_rect()
screen_rect = main_surface.get_rect()

# Center the image rect
picture_rect.center = screen_rect.center

# Scale the image if necessary
size = picture.get_size()
scale = aspect_scale(size)  # Define your aspect_scale function
picture = pygame.transform.scale(picture, scale)

# Blit the picture onto the main surface
main_surface.blit(picture, picture_rect)

# Update the display
pygame.display.update()

# Keep the window open until closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

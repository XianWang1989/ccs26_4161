
import pygame

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
picture = pygame.image.load(images[i])
size = picture.get_size()

# Scale the image
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the image and center it on the screen
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Blit the image onto the main surface
main_surface.blit(picture, picture_rect.topleft)

# Update the display
pygame.display.update()

# To keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

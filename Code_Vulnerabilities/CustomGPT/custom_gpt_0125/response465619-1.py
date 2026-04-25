
import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load(images[i])
size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, (scale))

# Center the image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Blit the image
main_surface.blit(picture, picture_rect.topleft)
pygame.display.update()

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

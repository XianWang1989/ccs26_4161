
import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load(images[i])  # Assume images[i] is your image path
size = picture.get_size()

# Scale the image if necessary (implement aspect_scale function as needed)
scale = aspect_scale(size)  # Example function to calculate scale based on your logic
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the picture
picture_rect = picture.get_rect()

# Centering the image in the main surface
picture_rect.center = (screen_width // 2, screen_height // 2)

# Blit the picture onto the main surface
main_surface.blit(picture, picture_rect.topleft)

# Update the display
pygame.display.update()

# Event loop (for closing the window properly)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

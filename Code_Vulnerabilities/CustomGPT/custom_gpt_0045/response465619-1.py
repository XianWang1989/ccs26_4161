
import pygame

# Initialize Pygame
pygame.init()

# Set up the main display surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load(images[i])
size = picture.get_size()

# Scale the image maintaining aspect ratio if needed
scale = aspect_scale(size)  # Ensure this function is defined; it should return appropriate dimensions
picture = pygame.transform.scale(picture, (scale))

# Create a rectangle for the image with its center at the center of the display
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Blit the image onto the main surface at the rect position
main_surface.blit(picture, picture_rect.topleft)

# Update the display
pygame.display.update()

# Main loop (you need to add your event handling loop here)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

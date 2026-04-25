
import pygame

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
picture = pygame.image.load(images[i])
size = picture.get_size()

# Function to calculate aspect scale (adjust as needed)
def aspect_scale(size):
    # Placeholder scaling logic. Change as needed for your use case.
    scale_factor = min(screen_width / size[0], screen_height / size[1])
    return int(size[0] * scale_factor), int(size[1] * scale_factor)

# Scale image
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Blit the image onto the main surface
main_surface.blit(picture, picture_rect)

# Update the display
pygame.display.update()

# Event loop (basic; adjust as needed)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

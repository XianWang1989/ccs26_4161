
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale image
image_path = "path/to/your/image.png"
picture = pygame.image.load(image_path)
size = picture.get_size()
scale = aspect_scale(size)  # Assume this function is defined to get the scaled size
picture = pygame.transform.scale(picture, (scale))

# Create a rect for the image centered on the screen
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main_surface.fill((0, 0, 0))  # Clear screen with black
    main_surface.blit(picture, picture_rect.topleft)  # Blit image at the top-left of the rect
    pygame.display.update()

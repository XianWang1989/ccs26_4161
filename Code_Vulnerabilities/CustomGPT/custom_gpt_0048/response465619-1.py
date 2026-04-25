
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
picture = pygame.image.load("path_to_your_image.png")
size = picture.get_size()
scale = (int(size[0] * aspect_scale), int(size[1] * aspect_scale))  # Assuming aspect_scale is defined
picture = pygame.transform.scale(picture, scale)

# Center the image
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    main_surface.fill((0, 0, 0))

    # Draw the image centered
    main_surface.blit(picture, picture_rect)
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

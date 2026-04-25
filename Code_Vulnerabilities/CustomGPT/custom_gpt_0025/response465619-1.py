
import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440
main_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load and scale image
image_path = "path/to/your/image.png"  # Replace with your image path
picture = pygame.image.load(image_path)
size = picture.get_size()
scale = aspect_scale(size)  # Assuming you have this function defined
picture = pygame.transform.scale(picture, (scale))

# Get rect and center it
picture_rect = picture.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    main_surface.fill((0, 0, 0))  # Fill with black or your desired background color

    # Blit picture
    main_surface.blit(picture, picture_rect.topleft)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()

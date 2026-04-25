
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
image_path = 'path/to/your/image.png'  # Update with your image path
picture = pygame.image.load(image_path)
size = picture.get_size()
scale = (size[0] // 2, size[1] // 2)  # Example scaling, adjust as needed
picture = pygame.transform.scale(picture, scale)

# Get the rect for positioning
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)  # Center the image

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_surface.fill((255, 255, 255))  # Fill the background with white
    main_surface.blit(picture, picture_rect)  # Draw the image at its rect
    pygame.display.update()

pygame.quit()
sys.exit()

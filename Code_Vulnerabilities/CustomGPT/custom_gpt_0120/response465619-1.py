
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
image_path = 'path/to/your/image.png'  # Update with the image path
picture = pygame.image.load(image_path)
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the image after scaling
picture_rect = picture.get_rect()

# Center the rect in the middle of the screen
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    main_surface.fill((0, 0, 0))  # Fill with black background

    # Blit the image at the centered position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

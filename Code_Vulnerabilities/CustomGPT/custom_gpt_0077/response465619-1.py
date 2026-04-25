
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
image_path = 'your_image.png'  # replace with your image path
picture = pygame.image.load(image_path)

# Scale image (modify aspect_scale to your needs)
def aspect_scale(size):
    # Example scale logic, replace with actual logic if needed
    max_size = (400, 400)  # maximum width, height
    return (min(size[0], max_size[0]), min(size[1], max_size[1]))

size = picture.get_size()
scale = aspect_scale(size)
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

    # Fill the screen with a background color (optional)
    main_surface.fill((0, 0, 0))  # black background

    # Blit the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

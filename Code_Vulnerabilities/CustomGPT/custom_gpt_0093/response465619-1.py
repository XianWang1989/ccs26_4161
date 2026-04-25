
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image if needed
def aspect_scale(size, target_width=800, target_height=600):
    width, height = size
    aspect_ratio = width / height
    if width > height:
        new_size = (target_width, int(target_width / aspect_ratio))
    else:
        new_size = (int(target_height * aspect_ratio), target_height)
    return new_size

# Center the image
size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (RGB)
    main_surface.fill((255, 255, 255))

    # Draw the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

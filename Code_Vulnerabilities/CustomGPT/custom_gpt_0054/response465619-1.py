
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
image_path = 'path/to/your/image.png'
picture = pygame.image.load(image_path)

# Calculate scaled size (assuming you have an aspect_scale function)
size = picture.get_size()
scale = aspect_scale(size)  # Replace with your own scaling logic
picture = pygame.transform.scale(picture, scale)

# Calculate position to center the image
picture_rect = picture.get_rect()
center_x = (screen_width - picture_rect.width) // 2
center_y = (screen_height - picture_rect.height) // 2

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))

    # Blit the image at the calculated position
    main_surface.blit(picture, (center_x, center_y))

    # Update the display
    pygame.display.update()

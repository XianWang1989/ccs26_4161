
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
image_path = 'path_to_your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)
size = picture.get_size()

# Scale the image if necessary
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scale to 50%
picture = pygame.transform.scale(picture, scale)

# Create a rectangle to center the image
picture_rect = picture.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black
    main_surface.fill((0, 0, 0))

    # Blit the image centered on the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

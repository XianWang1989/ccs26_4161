
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path_to_your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Get the original size and scale the image if needed
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling
picture = pygame.transform.scale(picture, scale)

# Get the rect of the image and center it on the screen
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    main_surface.fill((255, 255, 255))  # Fill with white for visibility

    # Blit the image centered on the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

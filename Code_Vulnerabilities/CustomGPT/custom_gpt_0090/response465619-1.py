
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the main surface (screen)
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'your_image.png'
picture = pygame.image.load(image_path)

# Scale the image if necessary
def aspect_scale(size):
    # Example scaling logic (modify as needed)
    return (int(size[0] * 0.5), int(size[1] * 0.5))

size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rect of the picture and center it on the screen
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    main_surface.fill((255, 255, 255))  # Optional: fill with white

    # Blit the image onto the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

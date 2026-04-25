
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the main surface
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
image_path = 'your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Get the rect of the image and center it
picture_rect = picture.get_rect()
picture_rect.center = main_surface.get_rect().center

# Scale the image if needed
def aspect_scale(size):
    # Modify this function as needed for scaling
    return (size[0] // 2, size[1] // 2)  # Example scaling

size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    # Fill the background
    main_surface.fill((0, 0, 0))  # Filling with black or your preferred color

    # Blit the image in the center
    main_surface.blit(picture, picture_rect.topleft)  # Use topleft for positioning

    # Update the display
    pygame.display.update()


import pygame

# Initialize Pygame
pygame.init()

# Set up the main surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path_to_your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Get the size of the image and scale if necessary
size = picture.get_size()
scale = aspect_scale(size)  # Assume this function is defined
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop (just for demonstration)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the surface
    main_surface.fill((0, 0, 0))  # Fill with black or any color

    # Blit the image onto the surface
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

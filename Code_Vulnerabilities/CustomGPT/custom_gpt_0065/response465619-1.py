
import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and center the image
image_path = 'path_to_your_image.png'  # Update with your image path
picture = pygame.image.load(image_path)
size = picture.get_size()
scale = aspect_scale(size)  # Assuming you have this function defined
picture = pygame.transform.scale(picture, (scale))

# Create a rectangle for positioning
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any color

    # Blit the picture onto the main surface
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

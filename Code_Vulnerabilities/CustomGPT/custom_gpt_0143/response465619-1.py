
import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
picture = pygame.image.load("your_image.png")  # Replace with your image path

# Scale image if needed (optional)
# size = picture.get_size()
# scale = aspect_scale(size)  # Define your aspect_scale function as necessary
# picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the main surface with a background color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the picture to the center
    main_surface.blit(picture, picture_rect.topleft)  # Use topleft for correct positioning

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

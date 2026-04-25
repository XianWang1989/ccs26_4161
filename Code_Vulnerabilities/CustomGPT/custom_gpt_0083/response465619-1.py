
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load("path_to_your_image.png")

# Scale the image if needed
def aspect_scale(size):
    # Example scaling logic (adjust as necessary)
    scale_factor = 0.5  # Scale down by 50%
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the image centered
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

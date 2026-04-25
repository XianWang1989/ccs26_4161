
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load and scale the image
picture = pygame.image.load('path/to/your/image.png')
size = picture.get_size()

# Define your aspect scaling function if needed
def aspect_scale(size):
    # Example scaling logic, adjust as needed
    scale_factor = min(screen_size[0] / size[0], screen_size[1] / size[1])
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Create a rect for positioning
picture_rect = picture.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    main_surface.fill((0, 0, 0))

    # Draw the image in the center
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

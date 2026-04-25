
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
image_path = "path/to/your/image.png"  # Replace with your image path
picture = pygame.image.load(image_path)
size = picture.get_size()

# Scale image if needed
scale = aspect_scale(size)  # Define your aspect_scale function
picture = pygame.transform.scale(picture, (scale))

# Get picture rectangle and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any color

    # Blit the picture at the centered rect
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

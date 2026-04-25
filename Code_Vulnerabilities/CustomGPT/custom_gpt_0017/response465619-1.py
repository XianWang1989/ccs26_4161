
import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale image
picture = pygame.image.load('your_image.png')  # Replace with your image path
size = picture.get_size()
scale = (int(size[0] / 2), int(size[1] / 2))  # Example scaling, adjust as needed
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the scaled picture
picture_rect = picture.get_rect()

# Center the rectangle
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the surface with a color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the picture at the center
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

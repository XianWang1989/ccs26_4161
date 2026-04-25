
import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path_to_your_image.png')
size = picture.get_size()
scale = aspect_scale(size)  # Your scaling function if needed
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the image
picture_rect = picture.get_rect()
# Center the rect in the middle of the screen
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background (optional)
    main_surface.fill((0, 0, 0))

    # Blit the picture
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

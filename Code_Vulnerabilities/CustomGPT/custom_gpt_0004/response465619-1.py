
import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('your_image.png')
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Adjust this scale factor as needed
picture = pygame.transform.scale(picture, scale)

# Get the new rectangle of the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the image centered
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

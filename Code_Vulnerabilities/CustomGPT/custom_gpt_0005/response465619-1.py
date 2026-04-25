
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path/to/your/image.png'
picture = pygame.image.load(image_path)

# Get the rectangle of the image
picture_rect = picture.get_rect()

# Center the image on the screen
center_x = (screen_width - picture_rect.width) // 2
center_y = (screen_height - picture_rect.height) // 2
picture_rect.topleft = (center_x, center_y)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((0, 0, 0))

    # Blit the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

pygame.quit()

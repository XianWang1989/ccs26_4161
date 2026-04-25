
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load("path_to_your_image.png")  # Replace with your image path

# Get the image size and compute the center position
picture_rect = picture.get_rect()
size = picture.get_size()
scale = aspect_scale(size)  # Your scaling function
scaled_picture = pygame.transform.scale(picture, (scale))

# Center the image
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Draw the scaled image
    main_surface.blit(scaled_picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

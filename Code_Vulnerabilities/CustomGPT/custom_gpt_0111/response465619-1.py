
import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = 'path_to_your_image.png'  # Update with your image path
picture = pygame.image.load(image_path)

# Get image size and create a rect for it
picture_rect = picture.get_rect()

# Scale the image (optional)
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling to 50%
picture = pygame.transform.scale(picture, scale)

# Get the new rect for the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((255, 255, 255))  # Fill with white

    # Blit the image centered
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()


import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
image_path = "path_to_your_image.png"  # Replace with your image path
picture = pygame.image.load(image_path)

# Get the center of the image
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Scale the image if needed
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scale to 50%
picture = pygame.transform.scale(picture, scale)

# Adjust center after scaling
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color
    main_surface.fill((0, 0, 0))

    # Blit the image centered
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

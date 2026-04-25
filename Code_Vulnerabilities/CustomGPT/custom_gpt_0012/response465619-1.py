
import pygame

# Initialize Pygame
pygame.init()

# Set up the main surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
image = pygame.image.load('your_image.png')  # Replace with your image path
size = image.get_size()
scale = aspect_scale(size)  # Assume this function keeps the aspect ratio, implement as needed
image = pygame.transform.scale(image, (scale))

# Create a rectangle for the scaled image
image_rect = image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)  # Center the image on the screen

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Draw the image centered
    main_surface.blit(image, image_rect.topleft)  # Use .topleft for the blit position
    pygame.display.update()

pygame.quit()

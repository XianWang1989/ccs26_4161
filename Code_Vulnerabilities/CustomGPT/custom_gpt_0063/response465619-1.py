
import pygame

# Initialize Pygame
pygame.init()

# Set up screen size
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
picture = pygame.image.load("path/to/your/image.png")
size = picture.get_size()
scale = aspect_scale(size)  # Replace this with your scaling logic
picture = pygame.transform.scale(picture, scale)

# Get the rect for the scaled image
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((0, 0, 0))  # Fill with black

    # Blit the image at its rect position
    main_surface.blit(picture, picture_rect.topleft)  # Use .topleft for blit

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

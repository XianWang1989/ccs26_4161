
import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
picture = pygame.image.load(images[i])
size = picture.get_size()
scale = aspect_scale(size)  # Define your aspect_scale function
picture = pygame.transform.scale(picture, (scale))

# Get the rect for the image and center it on the screen
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop to display the image
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((0, 0, 0))

    # Blit the image centered on the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

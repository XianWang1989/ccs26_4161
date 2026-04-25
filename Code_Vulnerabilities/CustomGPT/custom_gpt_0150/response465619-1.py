
import pygame

# Initialize Pygame
pygame.init()

# Set up the main surface
main_surface = pygame.display.set_mode((2560, 1440))

# Load the image
picture = pygame.image.load(images[i])
# Scale the image if necessary
size = picture.get_size()
scale = aspect_scale(size)  # Define this function based on your scaling logic
picture = pygame.transform.scale(picture, scale)

# Get the rect for the picture and center it
picture_rect = picture.get_rect(center=(main_surface.get_width() // 2, main_surface.get_height() // 2))

# Main loop to display the image
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the surface with a background color (optional)
    main_surface.fill((0, 0, 0))  # Dark background

    # Blit the picture centered on the surface
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

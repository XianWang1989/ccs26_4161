
import pygame

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load("path/to/your/image.png")
size = picture.get_size()

# Scale the image if necessary (implement aspect_scale as needed)
scale = aspect_scale(size)  # Assuming this function scales the image appropriately
picture = pygame.transform.scale(picture, (scale))

# Create a rectangle for the image and center it
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen with a color
    main_surface.fill((0, 0, 0))  # Black background

    # Draw the picture centered
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

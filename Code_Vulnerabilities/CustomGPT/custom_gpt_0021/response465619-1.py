
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
image_path = 'path_to_your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Get the rect of the image and scale it if needed
size = picture.get_size()
scale = aspect_scale(size)  # Assuming you have a function to handle scaling
picture = pygame.transform.scale(picture, (scale))

# Get the rect and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((0, 0, 0))  # Fill with black

    # Blit the image at the correct position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

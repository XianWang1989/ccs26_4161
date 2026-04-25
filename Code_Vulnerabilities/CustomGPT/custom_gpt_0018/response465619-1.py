
import pygame

# Initialize Pygame
pygame.init()

# Set up the main surface (screen)
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
image_path = 'path_to_your_image.png'  # Modify this with your image path
picture = pygame.image.load(image_path)

# Scale the image if needed (optional)
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scale to 50%
picture = pygame.transform.scale(picture, scale)

# Get the rect of the scaled image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any desired color

    # Blit the picture using its rect
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

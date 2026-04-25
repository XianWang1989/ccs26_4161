
import pygame

# Initialize Pygame
pygame.init()

# Set up the main surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Center Image Example")

# Load the image
image_path = 'path_to_your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image as needed
scale = (int(picture.get_width() * 0.5), int(picture.get_height() * 0.5))  # Example scaling to 50%
picture = pygame.transform.scale(picture, scale)

# Get the rectangle of the scaled image
picture_rect = picture.get_rect()

# Center the image on the screen
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background color
    main_surface.fill((0, 0, 0))  # Black background

    # Draw the centered image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()

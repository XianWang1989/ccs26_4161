
import pygame

# Initialize Pygame
pygame.init()

# Set screen size
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
picture = pygame.image.load('your_image.png')  # Replace with your image path

# Get the rectangle of the image and scale if necessary
picture_rect = picture.get_rect()
size = picture.get_size()
scale = aspect_scale(size)  # Implement your scaling logic here if needed
picture = pygame.transform.scale(picture, (scale))

# Center the image
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional, for visibility)
    main_surface.fill((255, 255, 255))

    # Draw the image centered on the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

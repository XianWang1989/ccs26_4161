
import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path/to/your/image.png')

# Get the size of the image
size = picture.get_size()

# Scale the image as needed (replace with your scaling logic)
def aspect_scale(size):
    scale_factor = 1  # Replace with your scaling logic
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

# Scale the image
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Get the rectangle of the image and center it
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop to display the image
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_surface.fill((0, 0, 0))  # Clear screen with black
    main_surface.blit(picture, picture_rect)  # Blit the image at its centered position
    pygame.display.update()

# Quit Pygame
pygame.quit()

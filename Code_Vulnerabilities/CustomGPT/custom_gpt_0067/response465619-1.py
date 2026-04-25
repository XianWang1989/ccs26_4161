
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Center Image Example")

# Load and scale the image
def load_and_center_image(image_path):
    picture = pygame.image.load(image_path)
    size = picture.get_size()
    # Aspect ratio scaling function (example placeholder)
    scale = aspect_scale(size)  # Implement your scaling logic here
    picture = pygame.transform.scale(picture, (scale))

    # Get the rectangle of the picture and center it on the screen
    picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

    # Blit the picture onto the surface
    main_surface.blit(picture, picture_rect.topleft)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    main_surface.fill((255, 255, 255))  # Fill the background with white
    load_and_center_image('path/to/your/image.png')  # Replace with your image path
    pygame.display.update()

pygame.quit()
sys.exit()

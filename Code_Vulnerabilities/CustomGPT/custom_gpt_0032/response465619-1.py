
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
image_path = "path/to/your/image.png"  # Update to your image path
picture = pygame.image.load(image_path)

# Scale image if necessary
def aspect_scale(size):
    # Implement your aspect scaling logic here if needed
    return size

size = picture.get_size()
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, (scale))

# Get the rectangle of the image and calculate the position
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)  # Center the image

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the image at the calculated position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

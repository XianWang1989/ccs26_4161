
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Center Image Example')

# Load the image
picture = pygame.image.load('your_image.png')  # Replace 'your_image.png' with your image path
size = picture.get_size()

# Scale the image if needed (optional)
def aspect_scale(size, target_size=(2560, 1440)):
    scale_factor = min(target_size[0] / size[0], target_size[1] / size[1])
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rect of the picture and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the background
    main_surface.fill((255, 255, 255))  # Fill with white color

    # Blit the picture at the center
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.flip()

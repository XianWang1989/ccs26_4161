
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load your image
image_path = 'path_to_your_image.png'
picture = pygame.image.load(image_path)

# Scale the image if needed
size = picture.get_size()
scale = aspect_scale(size)  # Make sure this function scales properly
picture = pygame.transform.scale(picture, (scale))

# Center the image
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black or any background color

    # Blit the image at the calculated position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

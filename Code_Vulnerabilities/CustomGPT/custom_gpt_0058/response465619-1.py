
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('your_image.png')  # Replace with your image path
size = picture.get_size()
scale = (int(size[0] * 1), int(size[1] * 1))  # Adjust scaling if needed
picture = pygame.transform.scale(picture, scale)

# Create a rect for the picture and center it on the screen
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    main_surface.fill((255, 255, 255))  # Fill the screen with white

    # Blit the image at its rect position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

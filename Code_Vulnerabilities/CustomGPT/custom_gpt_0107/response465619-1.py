
import pygame

# Initialize Pygame
pygame.init()

# Set up the main surface
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load("your_image.png")  # Replace with your image file
size = picture.get_size()
scale = aspect_scale(size)  # Assuming you have an aspect_scale function
picture = pygame.transform.scale(picture, scale)

# Create a rect for the image and center it on the screen
picture_rect = picture.get_rect()
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    main_surface.fill((0, 0, 0))  # Fill with black or any color you prefer
    # Blit the image
    main_surface.blit(picture, picture_rect)  # Blit at the rect position
    pygame.display.update()

pygame.quit()

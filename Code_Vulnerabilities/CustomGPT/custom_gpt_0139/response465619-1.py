
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 2560, 1440
main_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Center Image Example')

# Load image
# Assuming the image is in your working directory and named 'your_image.png'
picture = pygame.image.load('your_image.png')
size = picture.get_size()
scale = (width // 4, height // 4)  # Adjust the scale as needed
picture = pygame.transform.scale(picture, scale)

# Get the rect of the scaled image and position it at the center of the screen
picture_rect = picture.get_rect()
picture_rect.center = (width // 2, height // 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((0, 0, 0))

    # Blit the image at the center of the screen
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()

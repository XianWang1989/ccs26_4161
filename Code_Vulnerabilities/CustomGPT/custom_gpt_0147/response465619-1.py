
import pygame

# Initialize Pygame
pygame.init()

# Set up screen dimensions
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('path_to_your_image.jpg')  # Replace with your image path
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scale; adjust as necessary
picture = pygame.transform.scale(picture, scale)

# Get the rect for the image
picture_rect = picture.get_rect()

# Center the image on the screen
center_x = (screen_width - picture_rect.width) // 2
center_y = (screen_height - picture_rect.height) // 2

# Blit the image
main_surface.blit(picture, (center_x, center_y))

# Update the display
pygame.display.update()

# Main loop (to keep the window open)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

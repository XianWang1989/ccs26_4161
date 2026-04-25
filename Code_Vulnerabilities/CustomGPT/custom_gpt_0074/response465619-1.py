
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load("path/to/image.png")
size = picture.get_size()

# Calculate the center of the screen
center_x = screen_width // 2
center_y = screen_height // 2

# Calculate the top-left corner based on image size
top_left_x = center_x - size[0] // 2
top_left_y = center_y - size[1] // 2

# Blit the image onto the main surface
main_surface.blit(picture, (top_left_x, top_left_y))

# Update the display
pygame.display.update()

# Wait for a while (optional)
pygame.time.wait(2000)

# Quit Pygame
pygame.quit()

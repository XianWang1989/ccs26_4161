
import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 2560
screen_height = 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('your_image.png')  # Replace 'your_image.png' with your actual image path
picture_rect = picture.get_rect()

# Calculate the scale based on aspect ratio if needed
def aspect_scale(size):
    # Example scaling logic, adjust as necessary
    scale_factor = 0.5  # Scale down by 50%
    return (int(size[0] * scale_factor), int(size[1] * scale_factor))

# Scale the picture if required
size = picture.get_size()
scaled_size = aspect_scale(size)
picture = pygame.transform.scale(picture, scaled_size)

# Center the image
picture_rect.center = (screen_width // 2, screen_height // 2)

# Draw the image on the screen
main_surface.blit(picture, picture_rect)

# Update the display
pygame.display.update()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

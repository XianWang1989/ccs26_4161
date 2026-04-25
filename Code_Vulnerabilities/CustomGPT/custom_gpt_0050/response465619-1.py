
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
picture = pygame.image.load(images[i])
size = picture.get_size()

# Function to maintain aspect ratio
def aspect_scale(size, max_width, max_height):
    aspect_ratio = size[0] / size[1]
    if size[0] > max_width or size[1] > max_height:
        if aspect_ratio > 1:
            new_width = max_width
            new_height = max_width / aspect_ratio
        else:
            new_height = max_height
            new_width = max_height * aspect_ratio
        return (int(new_width), int(new_height))
    return size

# Scale the image
scale = aspect_scale(size, screen_width, screen_height)
picture = pygame.transform.scale(picture, scale)

# Get the rect for positioning
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    main_surface.fill((255, 255, 255))

    # Blit the image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

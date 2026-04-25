
import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load image
picture = pygame.image.load("path_to_your_image.png")
size = picture.get_size()

# Function to scale the image
def aspect_scale(size, max_size=(2560, 1440)):
    scale_ratio = min(max_size[0] / size[0], max_size[1] / size[1])
    return (int(size[0] * scale_ratio), int(size[1] * scale_ratio))

# Scale the image
scale = aspect_scale(size)
picture = pygame.transform.scale(picture, scale)

# Get the rectangle for positioning
picture_rect = picture.get_rect()
picture_rect.center = (screen_width / 2, screen_height / 2)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    main_surface.fill((0, 0, 0))

    # Blit the image centered
    main_surface.blit(picture, picture_rect.topleft)

    # Update display
    pygame.display.update()

# Quit Pygame
pygame.quit()

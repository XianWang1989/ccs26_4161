
import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
image_path = "path/to/your/image.png"  # Change this to your image path
picture = pygame.image.load(image_path)

# Scale the image if necessary
def aspect_scale(size):
    max_width = 2560
    max_height = 1440
    scale = min(max_width / size[0], max_height / size[1])
    return (int(size[0] * scale), int(size[1] * scale))

# Get the scaled size
scaled_size = aspect_scale(picture.get_size())
picture = pygame.transform.scale(picture, scaled_size)

# Get the rect object and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    main_surface.fill((0, 0, 0))  # Fill with black

    # Blit the centered image
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

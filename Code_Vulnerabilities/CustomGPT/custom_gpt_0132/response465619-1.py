
import pygame

# Initialize Pygame
pygame.init()

# Set screen size
screen_size = (2560, 1440)
main_surface = pygame.display.set_mode(screen_size)

# Load the image
image_path = 'path/to/your/image.png'
picture = pygame.image.load(image_path)

# Scale the picture (adjust as needed)
size = picture.get_size()
scale = (int(size[0] * 0.5), int(size[1] * 0.5))  # Example scaling factor
picture = pygame.transform.scale(picture, scale)

# Get the rect of the picture and center it on the screen
picture_rect = picture.get_rect(center=main_surface.get_rect().center)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color (optional)
    main_surface.fill((255, 255, 255))  # White background

    # Blit the centered image
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

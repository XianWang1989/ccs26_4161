
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
main_surface = pygame.display.set_mode((2560, 1440))

# Load your image
image_path = 'your_image.png'  # Replace with your image path
picture = pygame.image.load(image_path)

# Scale the image if needed
size = picture.get_size()
scale = (size[0] // 2, size[1] // 2)  # Example scaling
picture = pygame.transform.scale(picture, scale)

# Get the Rect for the image and center it
picture_rect = picture.get_rect(center=main_surface.get_rect().center)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a background color
    main_surface.fill((0, 0, 0))  # Black background

    # Blit the image at the calculated center position
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()

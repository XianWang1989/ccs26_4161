
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Center Image Example")

# Load and scale image
images = ['your_image.png']  # Replace with your actual image path
picture = pygame.image.load(images[0])  # Load the image
size = picture.get_size()  # Get original size

# Function to scale the image (Placeholder)
def aspect_scale(size):
    # Assuming you want to preserve aspect ratio (you can customize this)
    max_width, max_height = 800, 600  # Example max dimensions
    width_ratio = max_width / size[0]
    height_ratio = max_height / size[1]
    scale_ratio = min(width_ratio, height_ratio)
    return (int(size[0] * scale_ratio), int(size[1] * scale_ratio))

# Scale the image
scale = aspect_scale(size) 
picture = pygame.transform.scale(picture, scale)

# Get the rectangle for positioning
picture_rect = picture.get_rect()
# Center the image on the screen
picture_rect.center = (screen_width // 2, screen_height // 2)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with a color (black in this case)
    main_surface.fill((0, 0, 0))

    # Blit the image at the calculated position
    main_surface.blit(picture, picture_rect.topleft)

    # Update the display
    pygame.display.update()


import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load the image
picture = pygame.image.load('your_image_path.png')
size = picture.get_size()

# Optionally scale the image based on your aspect scale function
scale = aspect_scale(size)  # Adjust this function as needed
picture = pygame.transform.scale(picture, scale)

# Get rectangle of the image and center it
picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    main_surface.fill((255, 255, 255))  # Fill with a white background

    # Blit the image to the centered position
    main_surface.blit(picture, picture_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

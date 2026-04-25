
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
main_surface = pygame.display.set_mode((screen_width, screen_height))

# Load and scale the image
def load_and_center_image(image_path):
    picture = pygame.image.load(image_path)
    size = picture.get_size()

    # Define your aspect_scale function as needed
    def aspect_scale(size):
        scale_factor = min(screen_width / size[0], screen_height / size[1])
        return (int(size[0] * scale_factor), int(size[1] * scale_factor))

    scale = aspect_scale(size)
    picture = pygame.transform.scale(picture, scale)

    # Get the rectangle centered on the screen
    picture_rect = picture.get_rect(center=(screen_width // 2, screen_height // 2))
    return picture, picture_rect

# Main loop
def main():
    image_path = 'path/to/your/image.png'  # Replace with your image path
    picture, picture_rect = load_and_center_image(image_path)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        main_surface.fill((0, 0, 0))  # Fill the background
        main_surface.blit(picture, picture_rect)  # Draw the centered image
        pygame.display.update()

if __name__ == '__main__':
    main()

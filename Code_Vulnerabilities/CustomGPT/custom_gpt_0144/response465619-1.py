import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 2560, 1440
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Center Image Example")

# Load and scale the image
image = pygame.image.load("your_image.png")  # Replace with your image path
original_size = image.get_size()

# Function to scale while preserving aspect ratio
def aspect_scale(size, max_size):
    original_width, original_height = size
    max_width, max_height = max_size
    scale = min(max_width / original_width, max_height / original_height)
    return int(original_width * scale), int(original_height * scale)

scaled_size = aspect_scale(original_size, (screen_width, screen_height))
image = pygame.transform.scale(image, scaled_size)

# Get the rect and center it
image_rect = image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)

# Blit and update display
screen.fill((0, 0, 0))  # Clear screen with black
screen.blit(image, image_rect)
pygame.display.update()

# Keep the window open until closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

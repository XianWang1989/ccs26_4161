
# mainProgram.py
import pygame
import myModule  # Importing your custom module

# Initialize Pygame
pygame.init()

# Set up a display
screen = pygame.display.set_mode((800, 600))

# Create a sprite
sprite_image, sprite_rect = myModule.makeSprite('path/to/image.png', (100, 100))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill((255, 255, 255))  # Filling white
    # Update sprite
    myModule.updateSprite((sprite_image, sprite_rect))

    # Update the display
    pygame.display.flip()

pygame.quit()

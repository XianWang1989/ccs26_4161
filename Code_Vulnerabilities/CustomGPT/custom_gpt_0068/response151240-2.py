
import pygame
import myModule

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create a sprite using the module
sprite = myModule.makeSprite('path_to_image.png', (100, 100))

# Main game loop example
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprite using the module
    myModule.updateSprite(sprite, sprite[1], screen)

    pygame.display.flip()  # Update the display

pygame.quit()

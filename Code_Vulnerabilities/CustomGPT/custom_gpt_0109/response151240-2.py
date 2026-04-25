
import pygame
import myModule  # Importing your module

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create and update the sprite
sprite = myModule.makeSprite(50, 50)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprite on the screen
    myModule.updateSprite(sprite, (100, 100))

    pygame.display.flip()

pygame.quit()

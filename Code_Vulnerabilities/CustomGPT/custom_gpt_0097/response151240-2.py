
import pygame
import myModule  # Load your custom module

pygame.init()

# Create a sprite using your module
sprite = myModule.makeSprite(50, 50)

# Optionally update the sprite
myModule.updateSprite(sprite)

# Example of calling a pygame function directly
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


import pygame
import myModule  # Import your module

pygame.init()

# Create a sprite of size 50x50
sprite = myModule.makeSprite(50, 50)

# Update the sprite
myModule.updateSprite(sprite)

# Example of a pygame function call
pygame.display.set_mode((640, 480))
pygame.display.set_caption("Sprite Example")

# Main loop for pygame (placeholder)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

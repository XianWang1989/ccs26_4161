
import pygame
import myModule

pygame.init()

# Create a sprite
sprite = myModule.makeSprite(50, 100)  # Example dimensions

# Update the sprite
myModule.updateSprite(sprite)

# You can now use any pygame function
pygame.display.set_mode((800, 600))

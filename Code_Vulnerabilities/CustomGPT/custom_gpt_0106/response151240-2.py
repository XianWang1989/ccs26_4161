
import pygame
import myModule

# Initialize pygame
pygame.init()

# Create a sprite using the module
sprite = myModule.makeSprite(50, 50)

# Update the sprite
myModule.updateSprite(sprite)

# Continue with other pygame function calls
# pygame.display.update()

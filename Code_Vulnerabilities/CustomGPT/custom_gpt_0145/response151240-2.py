
# main.py
import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()

# Now call your module functions
sprite = myModule.makeSprite()  # This works because pygame is initialized in this context
myModule.updateSprite(sprite)

# Your additional pygame logic here, like game loop or other function calls
# pygame.functionCallFromPygame() would go here if needed

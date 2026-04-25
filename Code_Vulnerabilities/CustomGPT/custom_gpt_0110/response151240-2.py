
# main.py
import pygame
import myModule  # Importing your custom module

pygame.init()  # Initialize pygame

# Use functions from the module
sprite = myModule.makeSprite(50, 50)  # Create a sprite
myModule.updateSprite("example arg1", "example arg2")  # Update a sprite

# Additional pygame functionality can be invoked
pygame.display.set_mode((800, 600))
pygame.quit()


import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()

# Use the module's functions
sprite = myModule.makeSprite(50, 50)  # Create a sprite with width and height of 50
myModule.updateSprite("New Position", "New Size")

# Example call to a pygame function (assuming you need it)
pygame.display.set_mode((800, 600))

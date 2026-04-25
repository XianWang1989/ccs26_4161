
import pygame
import myModule  # Importing your custom module

# Initialize Pygame
pygame.init()

# Use the functions from myModule
sprite = myModule.makeSprite(50, 50)  # Create a sprite of size 50x50
myModule.updateSprite(sprite)  # Update the sprite

# Optionally display the sprite using Pygame's window (not shown here)
# and handle any other Pygame functionalities


# main_program.py
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Use functions from your custom module
sprite = myModule.makeSprite(64, 64)  # Create a sprite of size 64x64
myModule.updateSprite(sprite)

# Further Pygame function calls can be made here
pygame.display.set_mode((800, 600))  # Set up display
pygame.display.flip()  # Update the full display Surface to the screen

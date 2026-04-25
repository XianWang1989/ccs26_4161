
# main.py
import pygame
import myModule  # Import your custom module

# Initialize Pygame
pygame.init()

# Use functions from your module
myModule.makeSprite()  # Function called with pygame already set up
myModule.updateSprite()

# Other Pygame logic can follow
pygame.quit()

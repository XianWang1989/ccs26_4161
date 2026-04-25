
# main.py
import pygame
import myModule

# Initialize pygame
pygame.init()

# Use the functions from your module
myModule.makeSprite(("sprite_image.png", (100, 100)))
myModule.updateSprite(("sprite_id", "new_properties"))

# Call a Pygame function
pygame.display.set_mode((800, 600))  # Example of using a Pygame function


# main.py
import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()

# Create a sprite using your module's function
sprite = myModule.makeSprite(50, 50)  # Creates a 50x50 pixel sprite

# Update the sprite
myModule.updateSprite(sprite)  # Calls the update function

# You can use other pygame functions here
pygame.display.flip()  # This is a pygame display function example
# Don't forget to finish the program appropriately, handling pygame.quit() as needed

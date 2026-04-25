
# main.py
import pygame
import myModule  # Importing your custom module

pygame.init()  # Initialize pygame once in your main program
sprite = myModule.makeSprite()  # Use the function from your module
myModule.updateSprite(sprite)  # Update the sprite as needed
pygame.display.flip()  # Example call to update the display

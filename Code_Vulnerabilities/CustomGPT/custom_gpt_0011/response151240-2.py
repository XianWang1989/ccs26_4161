
import pygame
import myModule  # Importing the module

# Initialize pygame
pygame.init()

# Example usage of the module functions
sprite = myModule.makeSprite(100, 50)  # Create a sprite of width 100 and height 50
sprite = myModule.updateSprite(sprite, (200, 100))  # Update sprite to new dimensions (200, 100)

# Remember to clean up
pygame.quit()

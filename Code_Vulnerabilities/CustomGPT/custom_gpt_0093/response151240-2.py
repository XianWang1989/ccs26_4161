
import pygame
import myModule  # Import your custom module

pygame.init()  # Initialize pygame

# Create a sprite using your module
sprite = myModule.makeSprite(50, 100)  # Create a sprite of width 50 and height 100

# Update the sprite
myModule.updateSprite(sprite)

# Example of using a pygame function
# Assuming you have a screen variable initialized here
# screen.blit(sprite, (x, y))  # Example to draw the sprite on the screen
pygame.display.flip()  # Update the full display Surface to the screen

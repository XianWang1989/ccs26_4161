
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a sprite using myModule
sprite = myModule.makeSprite(100, 200)

# Update the sprite
myModule.updateSprite(100, 200)

# Use Pygame function
pygame.display.set_mode((640, 480))  # Set up the display
pygame.display.set_caption("Sprite Example")
# (Add your game loop and event handling here)
pygame.quit()

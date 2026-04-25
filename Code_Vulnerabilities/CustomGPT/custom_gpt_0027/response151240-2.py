
import pygame
import myModule   # Import your module first

# Initialize Pygame
pygame.init()

# Now, we can use the functions from myModule
myModule.makeSprite('Sprite1', (100, 100))
myModule.updateSprite('Sprite1', (150, 150))

# Remember to include other Pygame functions as needed
pygame.display.set_mode((800, 600))

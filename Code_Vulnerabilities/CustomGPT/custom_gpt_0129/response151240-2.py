
import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()

# Create a sprite of size 50x50 using myModule methods
sprite = myModule.makeSprite(50, 50)

# Update sprite position to (100, 100)
sprite = myModule.updateSprite(sprite, (100, 100))

# Add your pygame logic to display this sprite or handle game loop here

# Terminate pygame when done
pygame.quit()

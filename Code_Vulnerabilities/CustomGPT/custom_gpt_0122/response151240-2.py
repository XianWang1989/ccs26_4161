
import pygame
import myModule  # Your custom module

# Initialize pygame
pygame.init()

# Create a sprite using the function from your module
sprite = myModule.makeSprite(50, 50)  # Create a 50x50 pixel sprite

# Update the sprite using the function from your module
myModule.updateSprite(sprite)

# Now you can use other pygame functions as needed
screen = pygame.display.set_mode((800, 600))  # Create a window
screen.blit(sprite, (100, 100))  # Draw the sprite at (100, 100)

pygame.display.flip()  # Update the display


import pygame
import myModule  # Import your custom module

# Initialize Pygame
pygame.init()

# Create a sprite using myModule
sprite = myModule.makeSprite(50, 100)

# Update the sprite with new parameters
myModule.updateSprite(sprite, {'position': (10, 20)})

# Example of calling a Pygame function
pygame.display.set_mode((640, 480))
screen = pygame.display.get_surface()
screen.blit(sprite, (10, 20))
pygame.display.flip()


import pygame
import myModule

pygame.init()

# Create a sprite
my_sprite = myModule.makeSprite(50, 50)

# Update the sprite
myModule.updateSprite(my_sprite)

# Use other pygame functions
# For example, displaying it in a window
screen = pygame.display.set_mode((300, 300))
screen.blit(my_sprite, (100, 100))
pygame.display.flip()

# Remember to clean up pygame
pygame.quit()


# main.py
import pygame
import myModule

pygame.init()

# Create a sprite using your module
sprite = myModule.makeSprite(50, 50)

# Use the sprite
# Assuming you have a display setup
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Call additional Pygame functions
pygame.time.delay(2000)  # Keep the window open for 2 seconds
pygame.quit()

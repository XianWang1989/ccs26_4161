
import pygame
import myModule  # Import your custom module

pygame.init()  # Initialize pygame

# Using your module's functions
myModule.makeSprite("sprite_image.png", (100, 100))
myModule.updateSprite("current_sprite", (150, 150))

# Making a call to a pygame function
pygame.display.set_mode((800, 600))
pygame.display.update()

# Remember to quit pygame at the end
pygame.quit()

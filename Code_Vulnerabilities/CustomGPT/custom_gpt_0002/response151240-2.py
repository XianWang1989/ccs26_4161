
import pygame
import myModule  # Importing your custom module

pygame.init()
sprite = myModule.makeSprite(50, 50)  # Creating a sprite of size 50x50
myModule.updateSprite(sprite)  # Updating the sprite
pygame.display.set_mode((400, 400)).blit(sprite, (100, 100))  # Blitting sprite to screen
pygame.display.flip()

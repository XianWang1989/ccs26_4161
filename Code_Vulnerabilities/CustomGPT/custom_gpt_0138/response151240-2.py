
# main_program.py
import pygame
import myModule

pygame.init()

# Assume these are your sprite arguments
arg1 = "sprite_data"
arg2 = "position_data"

myModule.makeSprite(arg1, arg2)
myModule.updateSprite(arg1, arg2)

# Example of a pygame function call
pygame.display.flip()

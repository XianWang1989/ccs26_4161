
# main_program.py
import pygame
import myModule

pygame.init()

# Using the module and pygame together
sprite_image = 'path_to_your_sprite_image.png'
sprite = myModule.makeSprite(sprite_image)
myModule.updateSprite(sprite, (100, 200))

# Don't forget to use pygame's functionalities
# pygame.display.update()  # if you have a pygame display set up

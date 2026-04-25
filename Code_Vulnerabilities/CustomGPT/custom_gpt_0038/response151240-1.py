
import pygame

def makeSprite(arg1, arg2):
    # Use pygame to create a sprite
    sprite = pygame.Surface((arg1, arg2))  # create a surface with given dimensions
    return sprite

def updateSprite(sprite, position):
    # Update the sprite's position
    screen = pygame.display.get_surface()  # get the current display surface
    screen.blit(sprite, position)  # draw the sprite at the specified position


import pygame

def makeSprite(arg1, arg2):
    # Example implementation of sprite creation
    sprite = pygame.Surface((arg1, arg2))  # Create a surface
    return sprite

def updateSprite(sprite, position):
    # Example implementation of updating sprite position
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite_rect

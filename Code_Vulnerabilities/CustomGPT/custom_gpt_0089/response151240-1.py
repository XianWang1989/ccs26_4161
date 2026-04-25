
import pygame

def makeSprite(arg1, arg2):
    # Example sprite creation code
    sprite = pygame.Surface((arg1, arg2))  # Create a sprite surface
    return sprite

def updateSprite(sprite, position):
    # Example sprite update code
    sprite.rect = sprite.get_rect(topleft=position)
    return sprite

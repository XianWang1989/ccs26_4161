
import pygame  # This remains in your module

def makeSprite(arg1, arg2):
    # Example of creating a sprite
    sprite = pygame.Surface((arg1, arg2))
    return sprite

def updateSprite(sprite, position):
    # Example of updating sprite position
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite_rect

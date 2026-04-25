
import pygame

def makeSprite(arg1, arg2):
    # Example code to create a sprite
    sprite = pygame.Surface((arg1, arg2))  # Create a new surface for the sprite
    return sprite

def updateSprite(sprite, position):
    # Example code to update sprite position
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite_rect

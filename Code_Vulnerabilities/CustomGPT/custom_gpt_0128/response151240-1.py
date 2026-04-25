
import pygame

def makeSprite(arg1, arg2):
    # Create a sprite using Pygame
    sprite = pygame.Surface((arg1, arg2))  # Example: create a surface
    return sprite

def updateSprite(sprite, position):
    # Update the position of the sprite
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite_rect


import pygame

def makeSprite(arg1, arg2):
    sprite = pygame.Surface((arg1, arg2))  # Create a sprite with the given dimensions
    return sprite

def updateSprite(sprite, new_dimensions):
    sprite = pygame.transform.scale(sprite, new_dimensions)  # Update sprite dimensions
    return sprite

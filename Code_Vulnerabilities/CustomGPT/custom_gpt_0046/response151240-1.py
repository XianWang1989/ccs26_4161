
import pygame

def makeSprite(arg1, arg2):
    # Example sprite creation with pygame
    sprite = pygame.Surface((arg1, arg2))  # Create a surface with given dimensions
    return sprite

def updateSprite(sprite, position):
    # Update sprite's position
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite_rect

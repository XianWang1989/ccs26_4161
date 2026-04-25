
import pygame

def makeSprite(arg1, arg2):
    # Assuming arg1 and arg2 are necessary parameters for sprite creation
    sprite = pygame.Surface((arg1, arg2))  # Create a new surface as a sprite
    return sprite

def updateSprite(sprite, position):
    # Update the sprite's position
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite_rect

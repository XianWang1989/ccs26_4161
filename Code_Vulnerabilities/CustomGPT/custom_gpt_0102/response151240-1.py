
import pygame

def makeSprite(arg1, arg2):
    # Example sprite creation logic
    sprite = pygame.Surface((arg1, arg2))
    return sprite

def updateSprite(sprite, position):
    # Example logic to update the sprite's position
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite_rect

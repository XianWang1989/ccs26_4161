
import pygame

def makeSprite(arg1, arg2):
    # Example sprite creation using pygame
    sprite_image = pygame.Surface((arg1, arg2))
    # Other sprite setup code
    return sprite_image

def updateSprite(sprite, position):
    # Update sprite position with pygame
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite_rect

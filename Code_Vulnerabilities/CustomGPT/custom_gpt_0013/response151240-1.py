
import pygame

def makeSprite(arg1, arg2):
    # Example sprite creation using `arg1` and `arg2`
    sprite = pygame.Surface((arg1, arg2))
    sprite.fill((255, 0, 0))  # Fill with red color
    return sprite

def updateSprite(sprite, position):
    # Update sprite position
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite_rect

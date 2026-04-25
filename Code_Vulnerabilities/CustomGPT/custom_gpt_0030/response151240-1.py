
import pygame

def makeSprite(arg1, arg2):
    # Create a sprite (just a simple example)
    sprite = pygame.Surface((arg1, arg2))
    sprite.fill((255, 0, 0))  # Fill with red color
    return sprite

def updateSprite(sprite, position):
    # Update the sprite's position (dummy implementation)
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite_rect


import pygame

def makeSprite(arg1, arg2):
    # Create a sprite using pygame
    sprite = pygame.Surface((50, 50))
    sprite.fill((255, 0, 0))  # Fill the sprite with red color
    return sprite

def updateSprite(sprite, new_position):
    # Update sprite position (example logic)
    sprite_rect = sprite.get_rect(topleft=new_position)
    return sprite_rect

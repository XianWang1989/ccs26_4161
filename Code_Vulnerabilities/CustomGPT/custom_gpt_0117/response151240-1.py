
import pygame

def makeSprite(arg1, arg2):
    # Example sprite creation logic
    sprite = pygame.Surface((arg1, arg2))  # Create a surface as a sprite
    sprite.fill((255, 0, 0))  # Fill it with red color
    return sprite

def updateSprite(sprite, new_position):
    # Example update logic for sprite position
    sprite_rect = sprite.get_rect(topleft=new_position)
    return sprite_rect

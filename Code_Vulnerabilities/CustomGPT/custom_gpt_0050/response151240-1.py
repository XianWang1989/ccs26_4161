
import pygame

def makeSprite(arg1, arg2):
    # Example sprite creation code
    sprite = pygame.Surface((arg1, arg2))
    # You can add more code to customize the sprite
    return sprite

def updateSprite(sprite, position):
    # Example position update code
    spriteRect = sprite.get_rect()
    spriteRect.topleft = position
    return spriteRect

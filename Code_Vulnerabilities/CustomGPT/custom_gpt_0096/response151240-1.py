
import pygame

def makeSprite(arg1, arg2):
    # Example sprite creation code using pygame
    sprite = pygame.Surface((arg1, arg2))
    return sprite

def updateSprite(sprite, new_size):
    # Example sprite update, resizing the sprite
    return pygame.transform.scale(sprite, new_size)

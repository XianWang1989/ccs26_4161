
import pygame

def makeSprite(arg1, arg2):
    # Your sprite creation code here, using pygame
    sprite = pygame.Surface((arg1, arg2))
    return sprite

def updateSprite(sprite):
    # Your sprite update code here, using pygame
    sprite.fill((255, 0, 0))  # Fill the sprite with red color

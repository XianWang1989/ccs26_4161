
import pygame

def makeSprite(arg1, arg2):
    # Here you would use pygame to create a sprite
    sprite = pygame.Surface((arg1, arg2))
    return sprite

def updateSprite(sprite):
    # Here you would ideally update the sprite properties
    # For example, fill it with color
    sprite.fill((255, 0, 0))  # Filling with red color

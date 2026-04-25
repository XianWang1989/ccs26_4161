import pygame

def makeSprite(x, y):
    sprite = pygame.Rect(x, y, 50, 50)
    return sprite

def updateSprite(sprite, dx, dy):
    sprite.x += dx
    sprite.y += dy

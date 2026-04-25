
# myModule.py
import pygame  # It's still good practice to import pygame here

def makeSprite(color, position):
    sprite = pygame.Surface((50, 50))
    sprite.fill(color)
    return sprite, position

def updateSprite(sprite, position):
    # Potentially update the sprite's position here
    return sprite, position

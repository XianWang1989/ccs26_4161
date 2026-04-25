
import pygame

def makeSprite(x, y):
    sprite = pygame.Surface((50, 50))  # Create a simple sprite
    sprite.fill((255, 0, 0))  # Fill the sprite with red color
    return sprite, (x, y)

def updateSprite(sprite, position):
    screen = pygame.display.get_surface()
    screen.blit(sprite[0], position)


import pygame

def makeSprite(arg1, arg2):
    # Example sprite creation code
    sprite = pygame.Surface((arg1, arg2))
    return sprite

def updateSprite(sprite):
    # Example update code (e.g., blitting to the screen)
    print(f"Updating sprite of size: {sprite.get_size()}")

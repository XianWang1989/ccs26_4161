
import pygame

def makeSprite(arg1, arg2):
    # Creating a sprite using pygame
    sprite = pygame.Surface((arg1, arg2))  # Example: arg1 is width, arg2 is height
    sprite.fill((255, 0, 0))  # Filling the sprite with red color
    return sprite

def updateSprite(sprite, x, y):
    # This function will update the position of the sprite
    screen = pygame.display.get_surface()  # Get the current screen
    screen.blit(sprite, (x, y))  # Blit (draw) the sprite at position (x, y)

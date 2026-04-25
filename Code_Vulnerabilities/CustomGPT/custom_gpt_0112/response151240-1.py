
import pygame

def makeSprite(arg1, arg2):
    # Assuming arg1 is position and arg2 is image
    sprite = pygame.image.load(arg2)
    sprite_rect = sprite.get_rect(topleft=arg1)
    return sprite, sprite_rect

def updateSprite(sprite, sprite_rect):
    # Here you could update the sprite's position or other properties
    sprite_rect.x += 1  # Example update

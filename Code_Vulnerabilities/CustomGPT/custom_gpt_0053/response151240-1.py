
import pygame

def makeSprite(image_path, position):
    sprite_image = pygame.image.load(image_path)
    sprite_rect = sprite_image.get_rect(topleft=position)
    return sprite_image, sprite_rect

def updateSprite(sprite, position):
    sprite[1].topleft = position

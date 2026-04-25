
import pygame

def makeSprite(image_path, position):
    sprite = pygame.image.load(image_path)
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite, sprite_rect

def updateSprite(sprite, sprite_rect, screen):
    screen.blit(sprite, sprite_rect)

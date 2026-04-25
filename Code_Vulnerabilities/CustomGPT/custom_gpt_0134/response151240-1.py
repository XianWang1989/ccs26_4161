
import pygame

def makeSprite(image_path):
    sprite = pygame.image.load(image_path)
    return sprite

def updateSprite(sprite, position):
    screen.blit(sprite, position)

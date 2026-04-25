
import pygame

def makeSprite(image, position):
    sprite = pygame.image.load(image)
    return sprite, position  # Just an example return

def updateSprite(sprite, position, screen):
    screen.blit(sprite[0], sprite[1])  # sprite[0] is the image

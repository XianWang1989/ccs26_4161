
import pygame

def makeSprite(image, position):
    sprite = pygame.image.load(image)  # Load image using pygame
    sprite_rect = sprite.get_rect(topleft=position)
    return sprite, sprite_rect

def updateSprite(screen, sprite, sprite_rect):
    screen.blit(sprite, sprite_rect)  # Draw sprite on the screen

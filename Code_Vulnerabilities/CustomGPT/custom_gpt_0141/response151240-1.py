
# myModule.py
import pygame

def makeSprite(image_path, position):
    # Load an image and create a sprite
    sprite_image = pygame.image.load(image_path)
    sprite_rect = sprite_image.get_rect(topleft=position)
    return sprite_image, sprite_rect

def updateSprite(sprite, screen):
    # Update the sprite's position/render it on the screen
    screen.blit(sprite[0], sprite[1])

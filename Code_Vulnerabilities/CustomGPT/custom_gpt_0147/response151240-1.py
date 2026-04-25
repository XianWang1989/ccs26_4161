
# myModule.py
import pygame

def makeSprite(image_path, position):
    # Load the sprite image and set its position
    sprite_image = pygame.image.load(image_path)
    sprite_rect = sprite_image.get_rect(topleft=position)
    return sprite_image, sprite_rect

def updateSprite(sprite):
    # Update the sprite on the screen (assumes it’s part of your game loop)
    screen.blit(sprite[0], sprite[1])  # screen needs to be defined in your main program

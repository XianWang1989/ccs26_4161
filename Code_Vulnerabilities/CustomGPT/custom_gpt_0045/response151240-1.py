
import pygame

def makeSprite(image_path, position):
    # Create a new sprite and return it
    sprite_image = pygame.image.load(image_path)
    sprite_rect = sprite_image.get_rect(topleft=position)
    return sprite_image, sprite_rect

def updateSprite(sprite, movement_vector):
    # Update the sprite's position
    sprite[1].move_ip(movement_vector)

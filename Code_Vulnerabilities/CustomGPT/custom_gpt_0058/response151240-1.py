
import pygame

def makeSprite(arg1, arg2):
    # Assuming arg1 is an image and arg2 is position
    sprite = pygame.image.load(arg1)
    # Logic to create the sprite using pygame goes here
    print(f"Sprite created with image: {arg1} at position: {arg2}")

def updateSprite(arg1, arg2):
    # Assuming arg1 is the sprite and arg2 is new position
    # Logic to update the sprite using pygame goes here
    print(f"Sprite updated to new position: {arg2}")


import pygame

def makeSprite(arg1, arg2):
    # Assuming arg1 is an image and arg2 is a position
    sprite = pygame.image.load(arg1)  # Load the sprite image
    sprite_rect = sprite.get_rect(topleft=arg2)  # Get the rectangle for positioning
    return sprite, sprite_rect  # Return both the sprite and its position

def updateSprite(sprite, sprite_rect):
    # Function to draw the sprite on the screen
    screen = pygame.display.get_surface()  # Get the current display surface
    screen.blit(sprite, sprite_rect)  # Draw the sprite

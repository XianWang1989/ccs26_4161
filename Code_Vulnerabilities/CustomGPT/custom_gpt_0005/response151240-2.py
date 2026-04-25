
import pygame
import myModule  # Importing your custom module

pygame.init()  # Initialize Pygame

# Create a sprite using myModule
sprite = myModule.makeSprite(50, 50)
print(f"Sprite created with size: {sprite.image.get_size()}")

# Update the sprite position
myModule.updateSprite(sprite)
print(f"Sprite new position: {sprite.rect.x}")

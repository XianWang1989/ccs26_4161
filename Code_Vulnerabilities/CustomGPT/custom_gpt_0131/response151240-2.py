
import pygame
import myModule

pygame.init()

# Initialize sprite parameters
sprite_width = 50
sprite_height = 100
position = (10, 10)

# Create a sprite using myModule
sprite = myModule.makeSprite(sprite_width, sprite_height)

# Update the sprite (you would typically also handle the display)
myModule.updateSprite(sprite, position)

# Main game loop (showing an example of how to integrate with Pygame's event loop)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

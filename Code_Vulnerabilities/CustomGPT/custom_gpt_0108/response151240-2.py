
import pygame
import myModule  # Import your module

pygame.init()  # Initialize pygame

# Create a sprite using myModule
sprite = myModule.makeSprite(50, 50)

# Update the sprite
myModule.updateSprite(sprite)

# Example function call from pygame
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))  # Draw the sprite
pygame.display.flip()  # Update the display

# Run a simple loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

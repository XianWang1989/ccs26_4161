
import pygame  # Setup Pygame first
import myModule  # Now import the custom module

# Initialize pygame
pygame.init()

# Create sprite
sprite = myModule.makeSprite()

# Game loop (Simplified)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprite on the screen
    myModule.updateSprite(sprite)

pygame.quit()

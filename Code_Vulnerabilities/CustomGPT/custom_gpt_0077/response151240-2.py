
import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()

# Usage of the functions from myModule
sprite = myModule.makeSprite(50, 50)  # Create a sprite of 50x50
myModule.updateSprite(sprite)  # Update the sprite

# Your pygame game loop would go here
# For example, to display the sprite you would do something like:
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))  # Draw sprite at position (100, 100)
pygame.display.flip()

# Main loop (example)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


import pygame
import myModule  # Your module containing sprite functions

# Initialize Pygame
pygame.init()

# Create a sprite using your module
sprite = myModule.makeSprite(50, 50)  # Create a 50x50 sprite
myModule.updateSprite(sprite)  # Update the sprite

# To draw the sprite on the screen
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))  # Draw sprite at (100, 100)
pygame.display.flip()

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

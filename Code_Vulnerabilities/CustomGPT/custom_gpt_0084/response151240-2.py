
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Using the module function
sprite = myModule.makeSprite(50, 100)  # Create a sprite of size 50x100
myModule.updateSprite(sprite)

# Example of using a Pygame function after creating the sprite
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 150))  # Draw the sprite on the screen
pygame.display.flip()

# Run a simple loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

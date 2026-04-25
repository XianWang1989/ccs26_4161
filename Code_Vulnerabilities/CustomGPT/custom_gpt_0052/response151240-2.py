
import pygame
import myModule  # Import your custom module

# Initialize Pygame
pygame.init()

# Create a sprite using your module
sprite = myModule.makeSprite(50, 50)  # Creating a 50x50 sprite

# Update the sprite
myModule.updateSprite(sprite)

# Further Pygame code, e.g., display the sprite
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))  # Draw the sprite at (100, 100)
pygame.display.flip()

# Event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

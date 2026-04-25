
import pygame
import myModule  # Your custom module

pygame.init()  # Initialize Pygame

# Create a sprite using your module
sprite = myModule.makeSprite(50, 50)  # Example dimensions

# Update the sprite
myModule.updateSprite(sprite)

# Now, you can use Pygame functions directly
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))
pygame.display.flip()  # Update the display

# Main loop for the Pygame window (example)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

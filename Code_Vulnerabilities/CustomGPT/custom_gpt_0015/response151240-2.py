
import pygame
import myModule  # Import your custom module

pygame.init()  # Initialize Pygame

# Create a sprite using your module
sprite = myModule.makeSprite(50, 50)  # Create a sprite of size 50x50
myModule.updateSprite(sprite)  # Update the sprite

# Example of using another Pygame function
screen = pygame.display.set_mode((400, 300))
screen.blit(sprite, (100, 100))  # Draw the sprite on the screen

pygame.display.flip()  # Update the display

# Keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

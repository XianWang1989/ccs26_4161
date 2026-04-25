
import pygame
import myModule  # Your custom module

# Initialize pygame
pygame.init()

# Example usage of the module
sprite = myModule.makeSprite(50, 50)  # Create a sprite of size 50x50
myModule.updateSprite(sprite)  # Update the sprite

# Call other pygame functions
screen = pygame.display.set_mode((800, 600))  # Set up a display
screen.blit(sprite, (100, 100))  # Draw the sprite on the screen
pygame.display.flip()  # Update the full display Surface to the screen

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

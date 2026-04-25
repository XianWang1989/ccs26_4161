
import pygame
import myModule  # Importing your custom module

pygame.init()  # Initialize pygame

# Create a sprite using the custom module
sprite = myModule.makeSprite(50, 50)  # Create a 50x50 sprite

# Update the sprite
myModule.updateSprite(sprite)

# You can now use Pygame functions as needed
screen = pygame.display.set_mode((500, 500))
screen.blit(sprite, (100, 100))  # Draw the sprite at (100, 100)

pygame.display.flip()  # Update the full display Surface to the screen

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()  # Clean up pygame

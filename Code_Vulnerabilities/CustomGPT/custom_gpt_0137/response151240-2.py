
import pygame
import myModule  # Import your custom module

# Initialize Pygame
pygame.init()

# Use your module to create a sprite
sprite = myModule.makeSprite(50, 50)  # Create a sprite of size 50x50
updated_sprite = myModule.updateSprite(sprite)  # Update the sprite

# Example of how to use the sprite in a Pygame window
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the sprite onto the screen
    screen.blit(updated_sprite, (375, 275))  # Blit the sprite at position (375, 275)
    pygame.display.flip()  # Update the display

pygame.quit()


import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()

# Create a sprite using the module
sprite = myModule.makeSprite(50, 50)  # Create a 50x50 sprite
myModule.updateSprite(sprite)  # Update the sprite

# Example code to display the sprite (simple Pygame loop)
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen with black
    screen.blit(sprite, (375, 275))  # Draw sprite at position (375, 275)
    pygame.display.flip()  # Update the display

pygame.quit()

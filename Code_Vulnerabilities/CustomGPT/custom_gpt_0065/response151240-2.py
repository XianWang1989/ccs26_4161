
import pygame
import myModule  # Import your custom module

# Initialize Pygame
pygame.init()

# Create a sprite with given dimensions
sprite = myModule.makeSprite(50, 50)

# Update the sprite (e.g., color change)
myModule.updateSprite(sprite)

# Example code to display the sprite in a Pygame window
screen = pygame.display.set_mode((400, 300))
screen.blit(sprite, (100, 100))

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()

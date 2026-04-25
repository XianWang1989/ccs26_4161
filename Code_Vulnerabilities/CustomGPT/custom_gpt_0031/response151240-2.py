
import pygame
import myModule  # Import your custom module

pygame.init()

# Create a sprite using your module
sprite = myModule.makeSprite(50, 50)

# Update the sprite
myModule.updateSprite(sprite)

# Here you can use other pygame functionality
screen = pygame.display.set_mode((400, 300))
screen.blit(sprite, (100, 100))  # Draw the sprite on the screen
pygame.display.flip()

# Main loop (for demonstration)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

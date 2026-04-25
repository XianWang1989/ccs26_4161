
import pygame
import myModule  # Import your custom module

pygame.init()  # Initialize pygame

# Create a sprite
sprite = myModule.makeSprite(50, 50)  # Pass dimensions

# Update the sprite
myModule.updateSprite(sprite)

# You can now use other pygame functions
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Main loop (to keep the window open)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

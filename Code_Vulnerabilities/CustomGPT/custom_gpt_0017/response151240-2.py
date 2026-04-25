
# main.py
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a sprite using the module
sprite = myModule.makeSprite(50, 50)

# Use the sprite in your main loop or wherever needed
# For demonstration purposes, here’s a simple usage
screen = pygame.display.set_mode((400, 300))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Main loop (just for completeness)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


# main_program.py
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a sprite
sprite, position = myModule.makeSprite((255, 0, 0), (100, 100))
# Update the sprite (you would include logic to move it here)
sprite, position = myModule.updateSprite(sprite, position)

# Example of using a Pygame function
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, position)
pygame.display.flip()

# Main event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

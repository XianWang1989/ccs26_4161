
import pygame
import myModule

# Initialize pygame
pygame.init()

# Create a sprite
sprite = myModule.makeSprite(50, 50)

# Update the sprite
myModule.updateSprite(sprite)

# Use another pygame function
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

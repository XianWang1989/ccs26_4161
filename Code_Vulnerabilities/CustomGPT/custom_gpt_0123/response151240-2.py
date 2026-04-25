
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a sprite using the module function
sprite = myModule.makeSprite(50, 50)

# Update the sprite with some properties
myModule.updateSprite(sprite)

# Do additional Pygame operations
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

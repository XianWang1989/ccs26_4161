
import pygame
import myModule

# Initialize Pygame first
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Use the module
sprite = myModule.makeSprite('path/to/image.png')
myModule.updateSprite(sprite, (100, 100))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()

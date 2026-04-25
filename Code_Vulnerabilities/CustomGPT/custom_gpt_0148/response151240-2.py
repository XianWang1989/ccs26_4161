
import pygame
import myModule  # Import your custom module

pygame.init()  # Initialize pygame

# Using the module to create a sprite
sprite = myModule.makeSprite(50, 50)
myModule.updateSprite(sprite)

# You can now use pygame functions with the sprite
screen = pygame.display.set_mode((640, 480))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Main loop (keep the window open)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

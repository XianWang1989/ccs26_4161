
import pygame
import myModule

# Initialize pygame
pygame.init()

# Create a sprite using myModule
sprite = myModule.makeSprite(50, 50)

# Update the sprite
myModule.updateSprite(sprite)

# Use a pygame function
screen = pygame.display.set_mode((400, 300))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

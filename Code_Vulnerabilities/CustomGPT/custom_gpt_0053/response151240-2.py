
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a sprite
sprite = myModule.makeSprite('path/to/image.png', (50, 50))

# Update the sprite position
myModule.updateSprite(sprite, (100, 100))

# Example of using a Pygame function
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite[0], sprite[1])  # Draw the sprite on the screen
pygame.display.flip()

# Remember to handle events and quit properly
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

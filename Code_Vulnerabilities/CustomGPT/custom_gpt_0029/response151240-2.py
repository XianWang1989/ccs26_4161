
import pygame
import myModule  # Import your custom module here

# Initialize pygame
pygame.init()

# Create a sprite using the module's function
sprite = myModule.makeSprite(50, 50)

# Update the sprite as needed
myModule.updateSprite(sprite)

# Do something with pygame, like draw the sprite, etc.
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Main loop to keep the window open (simplified)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

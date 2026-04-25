
import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()

# Create a sprite using the function from your module
sprite = myModule.makeSprite(50, 50)

# Update the sprite in some way
myModule.updateSprite(sprite)

# You can now use other pygame functions
# For example, create a window and display the sprite (this is just an example)
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Keep the window open until you close it
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

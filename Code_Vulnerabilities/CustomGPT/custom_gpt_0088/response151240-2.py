
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a sprite using the module
sprite = myModule.makeSprite(50, 50)

# Update the sprite in your main loop (example loop)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    myModule.updateSprite(sprite)

    # You can now use other pygame functions as needed
    # pygame.display.flip() would typically go here

# Quit Pygame
pygame.quit()

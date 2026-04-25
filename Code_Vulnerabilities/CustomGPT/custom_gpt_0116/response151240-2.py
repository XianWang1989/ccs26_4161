
import pygame
import myModule  # Import your custom module

pygame.init()

# Create a sprite
sprite = myModule.makeSprite(0, 0)

# Main loop (just for example)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprite
    myModule.updateSprite(sprite)

pygame.quit()

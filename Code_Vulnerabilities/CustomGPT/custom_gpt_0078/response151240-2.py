
import pygame
import myModule  # Import your module

pygame.init()

# Setup screen
screen = pygame.display.set_mode((800, 600))

# Create a sprite using the module
sprite = myModule.makeSprite(50, 50)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprite
    myModule.updateSprite(sprite)

    # Draw the sprite on the screen
    screen.blit(sprite, (100, 100))
    pygame.display.flip()

pygame.quit()


import pygame
import myModule  # Your custom module

# Initialize Pygame
pygame.init()

# Create a sprite using the custom module
sprite = myModule.makeSprite(50, 50)

# Update the sprite
myModule.updateSprite(sprite)

# Display setup (for example)
screen = pygame.display.set_mode((400, 400))
screen.blit(sprite, (100, 100))

# Main loop (just for demonstration)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

# Quit Pygame
pygame.quit()


import pygame
import myModule

# Initialize pygame
pygame.init()

# Create a sprite using the module
sprite = myModule.makeSprite(50, 50)

# Main loop (example)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display and other operations
    pygame.display.flip()

# Clean up
pygame.quit()

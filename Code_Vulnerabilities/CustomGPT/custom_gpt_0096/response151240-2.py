
import pygame
import myModule

# Initialize pygame
pygame.init()

# Create a sprite
sprite = myModule.makeSprite(50, 50)

# Update sprite size
new_sprite = myModule.updateSprite(sprite, (100, 100))

# You can call other pygame functions as needed
pygame.display.set_mode((800, 600))
pygame.display.get_surface().blit(new_sprite, (100, 100))

# Don't forget to update the display and handle events
pygame.display.flip()
# Handling events (just an example)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

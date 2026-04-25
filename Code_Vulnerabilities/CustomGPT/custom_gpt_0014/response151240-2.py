
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a sprite using the module
sprite = myModule.makeSprite(50, 50)

# Update sprite's position
new_position = (100, 100)
sprite, new_position = myModule.updateSprite(sprite, new_position)

# Example of using another pygame function
pygame.display.set_mode((800, 600))
pygame.display.get_surface().blit(sprite, new_position)
pygame.display.flip()

# Keep the window open until closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


import pygame
import myModule

pygame.init()  # Initialize Pygame

# Create a sprite using your module
sprite = myModule.makeSprite(50, 50)

# Update sprite position (example)
new_sprite = myModule.updateSprite(sprite, (100, 100))

# Example Pygame display setup
screen = pygame.display.set_mode((800, 600))
screen.blit(new_sprite, (100, 100))
pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

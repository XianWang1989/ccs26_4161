
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a sprite using the module
sprite = myModule.makeSprite(50, 50)  # 50x50 sprite

# Updating the sprite position
sprite_rect = myModule.updateSprite(sprite, (100, 100))

# Example of using a Pygame function
screen = pygame.display.set_mode((400, 400))
screen.blit(sprite, sprite_rect)  # Draw sprite on the screen
pygame.display.flip()

# Main loop (simple)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

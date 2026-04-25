
import pygame
import myModule

# Initialize pygame
pygame.init()

# Use the myModule functions
sprite = myModule.makeSprite(50, 50)
sprite_rect = myModule.updateSprite(sprite, (100, 100))

# You can continue using pygame functions
pygame.display.set_mode((800, 600))
window = pygame.display.set_mode((800, 600))

# Main loop (simplified)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((0, 0, 0))  # Clear screen
    window.blit(sprite, sprite_rect)  # Draw the sprite
    pygame.display.flip()  # Update the display

pygame.quit()

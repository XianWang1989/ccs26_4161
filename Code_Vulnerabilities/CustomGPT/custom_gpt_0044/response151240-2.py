
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a sprite with dimensions
sprite = myModule.makeSprite(50, 50)

# Update the sprite position
position = (100, 150)
sprite_rect = myModule.updateSprite(sprite, position)

# You can use other Pygame functions after initializing
pygame.display.set_mode((800, 600))
screen = pygame.display.get_surface()
screen.blit(sprite, sprite_rect)

# Updating the display
pygame.display.flip()

# Main loop (basic)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

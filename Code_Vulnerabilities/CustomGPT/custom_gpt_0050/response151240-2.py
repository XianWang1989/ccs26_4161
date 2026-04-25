
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a sprite using the custom module
my_sprite = myModule.makeSprite(50, 50)

# Update sprite's position
sprite_rect = myModule.updateSprite(my_sprite, (100, 100))

# Example of handling Pygame display and events (minimal)
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))
screen.blit(my_sprite, sprite_rect.topleft)
pygame.display.flip()

# Main loop (for example purposes)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

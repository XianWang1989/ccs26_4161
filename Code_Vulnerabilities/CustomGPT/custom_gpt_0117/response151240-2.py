
import pygame
import myModule

# Initialize pygame
pygame.init()

# Create a sprite using myModule
sprite = myModule.makeSprite(50, 50)

# Update the sprite position
sprite_rect = myModule.updateSprite(sprite, (100, 100))

# Display your sprite (example with a simple window)
screen = pygame.display.set_mode((400, 400))
screen.blit(sprite, sprite_rect.topleft)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()

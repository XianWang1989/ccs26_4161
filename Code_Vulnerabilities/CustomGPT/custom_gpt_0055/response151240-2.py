
import pygame
import myModule  # Import your custom module

pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))

# Create a sprite using your module
sprite = myModule.makeSprite(50, 50)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprite position
    sprite_rect = myModule.updateSprite(sprite)

    # Draw the sprite on the screen
    screen.fill((0, 0, 0))  # Clear screen
    screen.blit(sprite, sprite_rect)
    pygame.display.flip()

pygame.quit()

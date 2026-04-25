
import pygame
import myModule  # Import the custom module

# Initialize Pygame
pygame.init()

# Create a sprite using the module
sprite = myModule.makeSprite(50, 50)  # Create a 50x50 sprite
sprite_rect = myModule.updateSprite(sprite, (100, 100))  # Update sprite position

# Main loop (example)
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen
    screen.blit(sprite, sprite_rect.topleft)  # Draw the sprite
    pygame.display.flip()  # Update display

pygame.quit()

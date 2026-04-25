
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a sprite
sprite = myModule.makeSprite(50, 50)  # Example: make a 50x50 sprite

# Update sprite position
sprite_rect = myModule.updateSprite(sprite, (100, 100))

# Main loop (simplified)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the sprite on the screen (assuming you have a screen)
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))  # Fill the background
    screen.blit(sprite, sprite_rect.topleft)  # Draw the sprite
    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()

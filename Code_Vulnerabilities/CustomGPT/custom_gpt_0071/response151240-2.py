
import pygame
import myModule  # Import your module

# Initialize Pygame
pygame.init()

# Create a sprite using our module
sprite = myModule.makeSprite()

# Update the sprite
sprite_rect = myModule.updateSprite(sprite)

# Example to display the sprite (in a Pygame window)
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))  # Fill the screen with white
screen.blit(sprite, sprite_rect.topleft)  # Draw the sprite
pygame.display.flip()

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

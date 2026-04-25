
import pygame
import myModule  # Import your custom module

pygame.init()  # Initialize pygame

# Create a sprite using the function from your module
sprite = myModule.makeSprite(50, 50)  # Create a 50x50 sprite
position = (100, 100)  # Position for the sprite

# Update sprite's position
sprite_rect = myModule.updateSprite(sprite, position)

# Main loop (simplified example)
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(sprite, sprite_rect)  # Draw the sprite on the screen
    pygame.display.flip()  # Update the display

pygame.quit()


import pygame
import myModule  # Import your custom module

# Initialize Pygame
pygame.init()

# Create a sprite using the module function
sprite = myModule.makeSprite(50, 100)  # Create a sprite of size 50x100
position = (10, 20)  # Position where the sprite will be rendered

# Update the sprite's position
sprite_rect = myModule.updateSprite(sprite, position)

# Example of using a Pygame function
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, sprite_rect)  # Draw the sprite on the screen

pygame.display.flip()  # Update the display

# Keep the window open until closed by the user
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

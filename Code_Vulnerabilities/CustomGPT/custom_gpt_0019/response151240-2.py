
import pygame
import myModule  # Importing the custom module

# Initialize Pygame
pygame.init()

# Create a sprite using the module
sprite = myModule.makeSprite(50, 50)  # Create a 50x50 sprite
myModule.updateSprite(sprite)  # Update the sprite's appearance

# Now you can use any pygame function
# Example: Creating a window to display the sprite
screen = pygame.display.set_mode((400, 400))
screen.blit(sprite, (100, 100))  # Draw the sprite at position (100, 100)
pygame.display.flip()  # Update the display

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

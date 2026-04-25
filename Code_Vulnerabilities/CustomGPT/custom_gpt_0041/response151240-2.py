
import pygame
import myModule  # Import your custom module

# Initialize Pygame
pygame.init()

# Use your module functions
sprite = myModule.makeSprite(50, 50)  # Create a sprite of size 50x50
myModule.updateSprite(sprite)  # Update the sprite

# Now you can use any Pygame functions
# For example, create a window to display the sprite
screen = pygame.display.set_mode((400, 300))
screen.blit(sprite, (100, 100))  # Draw the sprite at position (100, 100)
pygame.display.flip()  # Update the display

# Main loop for event handling
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

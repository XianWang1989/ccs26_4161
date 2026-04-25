
import pygame
import myModule  # Importing your custom module

# Initialize Pygame
pygame.init()

# Use the module functions
sprite = myModule.makeSprite(50, 50)  # Create a sprite of size 50x50
myModule.updateSprite(sprite)           # Update the created sprite

# Now you can use sprite with other Pygame functions
screen = pygame.display.set_mode((800, 600))  # Create a Pygame window
screen.blit(sprite, (100, 100))  # Draw the sprite at position (100, 100)
pygame.display.flip()  # Update the display

# Keep the window open until closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


import pygame
import myModule  # Import your custom module

# Initialize Pygame
pygame.init()

# Create a sprite using the module
sprite = myModule.makeSprite("arg1", "arg2")

# Do something with the sprite (like adding it to a game loop or drawing it)
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))  # Draw the sprite at position (100, 100)

# Update or manipulate the sprite as needed
myModule.updateSprite(sprite)

# Display the screen
pygame.display.flip()

# Event loop (simple version)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


import pygame
import myModule  # Import your module

# Initialize pygame
pygame.init()

# Create a sprite using your module's function
my_sprite = myModule.makeSprite()

# Use pygame's functionality to display the sprite, for example
screen = pygame.display.set_mode((800, 600))
screen.blit(my_sprite, (100, 100))  # Draw the sprite on the screen
pygame.display.flip()

# Update the sprite
myModule.updateSprite(my_sprite)

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

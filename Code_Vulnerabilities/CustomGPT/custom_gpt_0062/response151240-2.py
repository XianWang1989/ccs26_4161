
import pygame
import myModule  # your custom module

# Initialize pygame
pygame.init()

# Create sprites
sprite1 = myModule.makeSprite(50, 50)  # Create a sprite with size 50x50
myModule.updateSprite(sprite1)  # Update the created sprite

# Use a Pygame function
screen = pygame.display.set_mode((800, 600))  # Create a screen to display
screen.blit(sprite1, (100, 100))  # Draw the sprite on the screen

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

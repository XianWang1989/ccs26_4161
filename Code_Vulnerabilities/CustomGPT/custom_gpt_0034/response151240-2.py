
import pygame
import myModule

pygame.init()  # Initialize pygame

# Create a sprite using myModule
sprite = myModule.makeSprite(0, 0)

# You can use pygame functions directly here
screen = pygame.display.set_mode((800, 600))  # Set up the display
screen.blit(sprite, (100, 100))  # Draw the sprite
pygame.display.flip()  # Update the display

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()  # Clean up when done


import pygame
import myModule

pygame.init()  # Initialize pygame

# Create a sprite using the module function
sprite = myModule.makeSprite(64, 64)

# Update the sprite
myModule.updateSprite(sprite)

# If using other pygame functionalities:
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))  # Draw the sprite on the screen
pygame.display.flip()  # Update the display

# Main loop (add your event handling here)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

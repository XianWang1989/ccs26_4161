
import pygame
import myModule  # Your custom module

# Initialize Pygame
pygame.init()

# Use the functions from myModule
sprite = myModule.makeSprite(50, 50)
myModule.updateSprite(sprite)

# Example of additional Pygame functionality
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))  # Fill the screen with white
screen.blit(sprite, (100, 100))  # Draw the sprite on the screen
pygame.display.flip()

# Main loop to keep window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

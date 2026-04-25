
import pygame
import myModule  # Import your module

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))  # Set up a screen
sprite = myModule.makeSprite(50, 50)  # Create a sprite of size 50x50

# Main loop example
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen with black color
    myModule.updateSprite(sprite, 100, 100)  # Update and draw the sprite at position (100, 100)

    pygame.display.flip()  # Update the display

pygame.quit()

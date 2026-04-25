
import pygame
import myModule  # Import your custom module

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))  # Set up the display

# Create a sprite
sprite = myModule.makeSprite(50, 50)  # Create a sprite of size 50x50

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen with black
    myModule.updateSprite(sprite, (100, 100))  # Update and draw sprite
    pygame.display.flip()  # Refresh the display

pygame.quit()

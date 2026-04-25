
import pygame
import myModule  # Import your custom module

pygame.init()  # Initialize pygame
screen = pygame.display.set_mode((800, 600))  # Create a display surface

# Create a sprite using your module
sprite = myModule.makeSprite(50, 50)  # Create a red sprite

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen
    myModule.updateSprite(sprite, (100, 100))  # Update sprite's position
    pygame.display.flip()  # Update the display

pygame.quit()

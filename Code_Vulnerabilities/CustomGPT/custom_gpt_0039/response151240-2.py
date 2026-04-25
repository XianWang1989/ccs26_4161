
import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()

# Use your module's function to create a sprite
sprite = myModule.makeSprite(50, 50)  # Create a sprite of size 50x50

# Update the sprite (dummy call)
myModule.updateSprite(sprite)

# Example of displaying the sprite within a pygame loop
screen = pygame.display.set_mode((800, 600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a color
    screen.fill((255, 255, 255))

    # Draw the sprite onto the screen
    screen.blit(sprite, (100, 100))  # Draw sprite at (100, 100)

    pygame.display.flip()  # Update the display

pygame.quit()


import pygame
import myModule  # assuming myModule contains the above code

# Initialize Pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))

# Use the module to create a sprite
sprite = myModule.makeSprite('path/to/image.png', (10, 10))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprite position
    myModule.updateSprite(sprite, (1, 0))  # Move right

    # Clear screen and draw sprite
    screen.fill((0, 0, 0))  # Clear screen with black
    screen.blit(sprite[0], sprite[1])  # Draw sprite
    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()

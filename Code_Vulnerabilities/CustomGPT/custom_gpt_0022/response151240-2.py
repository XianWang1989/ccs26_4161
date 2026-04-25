
import pygame
import myModule

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create a sprite using your module
sprite = myModule.make_sprite(50, 50)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprite on the screen
    myModule.update_sprite(sprite, (100, 100))

    pygame.display.flip()

# Quit Pygame
pygame.quit()

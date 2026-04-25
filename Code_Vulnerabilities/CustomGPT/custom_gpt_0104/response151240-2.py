
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Create a sprite
sprite, sprite_rect = myModule.makeSprite('path_to_image.png', (50, 50))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update the sprite on the screen
    myModule.updateSprite(sprite, sprite_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

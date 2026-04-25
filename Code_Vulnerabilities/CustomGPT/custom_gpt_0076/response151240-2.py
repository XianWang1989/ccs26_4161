
import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
running = True

# Create a sprite
sprite, sprite_rect = myModule.makeSprite('path_to_image.png', (100, 100))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the sprite in your main loop
    screen.fill((255, 255, 255))  # Clear the screen
    myModule.updateSprite(sprite, sprite_rect, screen)

    pygame.display.flip()  # Update the display

pygame.quit()

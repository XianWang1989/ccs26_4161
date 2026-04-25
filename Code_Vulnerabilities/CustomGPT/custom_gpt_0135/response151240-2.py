
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
running = True

# Create a sprite
sprite, sprite_rect = myModule.makeSprite('path_to_image.png', (100, 100))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Clear the screen
    myModule.updateSprite(screen, sprite, sprite_rect)  # Update the sprite
    pygame.display.flip()  # Refresh the display

pygame.quit()

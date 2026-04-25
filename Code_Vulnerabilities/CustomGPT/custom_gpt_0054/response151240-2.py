
import pygame
import myModule  # Your custom module

pygame.init()  # Initialize Pygame

# Create a window
screen = pygame.display.set_mode((800, 600))

# Create a sprite using functions from myModule
sprite_image, sprite_rect = myModule.makeSprite('path/to/image.png', (100, 100))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprite position
    sprite_rect = myModule.updateSprite(sprite_image, sprite_rect)

    # Draw the sprite
    screen.fill((255, 255, 255))  # Clear the screen with white
    screen.blit(sprite_image, sprite_rect)  # Draw the sprite
    pygame.display.flip()  # Update the display

pygame.quit()

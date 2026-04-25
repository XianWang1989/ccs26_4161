
import pygame
import myModule

# Initialize pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Create a sprite
sprite, sprite_rect = myModule.makeSprite((50, 50), 'path/to/image.png')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen
    screen.blit(sprite, sprite_rect)  # Draw sprite
    pygame.display.flip()  # Update display

pygame.quit()


import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create a sprite
sprite = myModule.makeSprite(100, 100)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen
    myModule.updateSprite(sprite, sprite[1])  # Draw sprite

    pygame.display.flip()  # Update the full display

pygame.quit()

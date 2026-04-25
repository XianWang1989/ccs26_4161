
import pygame
import myModule  # Importing your module

# Initialize pygame
pygame.init()

# Create a sprite using myModule
sprite = myModule.makeSprite(50, 50)  # Creating a sprite with width=50 and height=50

# Update the sprite's position
sprite_rect = myModule.updateSprite(sprite, (100, 100))  # Move sprite to (100, 100)

# Optionally, use other pygame functions
screen = pygame.display.set_mode((800, 600))
screen.fill((0, 0, 0))  # Clear screen with black
screen.blit(sprite, sprite_rect.topleft)  # Draw the sprite
pygame.display.flip()  # Update the display

# Run a basic game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

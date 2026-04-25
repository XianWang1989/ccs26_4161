
import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()

# Create a sprite using myModule's function
sprite = myModule.makeSprite(50, 50)  # Width: 50, Height: 50

# Update the sprite position
sprite_rect = myModule.updateSprite(sprite, (100, 100))  # Position the sprite at (100, 100)

# Main loop or other pygame functionality can go here

# Example of using a pygame function
pygame.display.set_mode((800, 600))
screen = pygame.display.get_surface()
screen.blit(sprite, sprite_rect.topleft)
pygame.display.flip()

# To keep the window open, add an event loop here
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

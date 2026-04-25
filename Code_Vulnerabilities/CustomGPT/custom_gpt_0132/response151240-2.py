
import pygame
import myModule  # Import your custom module

# Initialize Pygame
pygame.init()

# Create a sprite using your module
sprite = myModule.makeSprite(50, 50)

# Update the sprite
myModule.updateSprite(sprite)

# For demonstration, show sprite in a Pygame window
screen = pygame.display.set_mode((200, 200))
screen.blit(sprite, (75, 75))
pygame.display.flip()

# Event loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

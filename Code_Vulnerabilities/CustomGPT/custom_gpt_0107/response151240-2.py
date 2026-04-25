
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Create a Sprite
sprite = myModule.makeSprite()

# Update the Sprite (just an example with no movement)
sprite = myModule.updateSprite(sprite)

# Display the sprite in the Pygame window
screen = pygame.display.set_mode((400, 400))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()

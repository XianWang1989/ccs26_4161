
import pygame
import myModule

# Initialize Pygame in the main program
pygame.init()

# Use functions from your module
sprite = myModule.makeSprite(50, 50)  # Create a sprite of size 50x50
position = (100, 100)
myModule.updateSprite(sprite, position)

# You can call any other Pygame functions here
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))  # Fill screen with white
screen.blit(sprite, sprite.rect.topleft)  # Draw the sprite
pygame.display.flip()  # Update the display

# Main loop (simplified)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()


import pygame
import myModule

pygame.init()

# Initialize sprite
sprite = myModule.makeSprite(50, 50)  # Create a sprite with width and height
position = (100, 150)

# Update sprite position
sprite_rect = myModule.updateSprite(sprite, position)

# Use other pygame functions
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))  # Fill the screen with white
screen.blit(sprite, sprite_rect)  # Draw the sprite
pygame.display.flip()  # Update the full display surface to the screen

# Main loop (just for demonstration)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

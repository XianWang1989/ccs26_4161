
import pygame
import myModule

# Initialize Pygame
pygame.init()

# Use the module to create and update a sprite
sprite = myModule.makeSprite(50, 50)
myModule.updateSprite(sprite)

# Continue with other pygame operations, such as displaying the sprite
# Example game loop (simplified)
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Clear screen
    screen.blit(sprite, (100, 100))  # Draw the sprite
    pygame.display.flip()  # Update the display

pygame.quit()


import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()

# Create a sprite using the module
sprite = myModule.makeSprite(50, 50)
print("Sprite created:", sprite)

# Update the sprite using the module
myModule.updateSprite(sprite)

# Use a Pygame function
pygame.display.set_mode((800, 600))
pygame.display.set_caption('Sprite Example')

# Main loop (placeholder)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

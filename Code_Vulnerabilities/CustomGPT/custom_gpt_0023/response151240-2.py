
import pygame
import my_module  # Importing your custom module

# Initialize pygame
pygame.init()

# Use the module to create and update sprites
sprite = my_module.makeSprite(50, 50)
my_module.updateSprite(sprite)

# Now you can use pygame functions
# For example, display the sprite on a window
screen = pygame.display.set_mode((800, 600))
screen.blit(sprite, (100, 100))
pygame.display.flip()

# Main loop to keep the window open (simple example)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

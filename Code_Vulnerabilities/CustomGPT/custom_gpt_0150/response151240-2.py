
import pygame
import myModule  # Import your module

# Initialize pygame first
pygame.init()

# Create a sprite using your module function
sprite = myModule.make_sprite(arg1=None, arg2=None)

# Now you can draw it on the screen or update it
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))  # Fill the screen with white
screen.blit(sprite, (100, 100))  # Draw the sprite at (100, 100)
pygame.display.flip()

# Main loop to keep the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

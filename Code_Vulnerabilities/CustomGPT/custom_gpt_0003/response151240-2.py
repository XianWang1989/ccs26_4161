
# main_program.py
import pygame
import myModule  # Import your custom module

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))

# Example positions for sprites
sprite_position = (100, 100)

# Create a sprite using myModule
myModule.makeSprite(screen, sprite_position)
pygame.display.flip()  # Update the display

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Don't forget to quit Pygame cleanly
pygame.quit()

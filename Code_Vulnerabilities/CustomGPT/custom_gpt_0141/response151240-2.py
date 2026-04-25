
# main_program.py
import pygame
import myModule  # Importing your custom module

# Initialize Pygame
pygame.init()

# Create a display surface
screen = pygame.display.set_mode((800, 600))

# Create a sprite
sprite = myModule.makeSprite("path_to_image.png", (50, 50))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Update and render the sprite
    myModule.updateSprite(sprite, screen)

    # Update the full display Surface to the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()

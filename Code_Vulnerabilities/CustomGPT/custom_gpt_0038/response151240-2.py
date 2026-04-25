
import pygame
import myModule  # Import your module

pygame.init()
screen = pygame.display.set_mode((800, 600))  # Create a screen for display

sprite = myModule.makeSprite(50, 50)  # Create a sprite with dimensions 50x50
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen with black color
    myModule.updateSprite(sprite, (100, 100))  # Update sprite position
    pygame.display.flip()  # Update the full display surface to the screen

pygame.quit()


import pygame
import myModule  # Import your module

pygame.init()
screen = pygame.display.set_mode((800, 600))  # Set up the screen

# Create a sprite
my_sprite = myModule.makeSprite(50, 50)  # Example sprite size 50x50

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen with a black color

    myModule.updateSprite(my_sprite, (100, 100))  # Update the sprite position
    pygame.display.flip()  # Update the display

pygame.quit()

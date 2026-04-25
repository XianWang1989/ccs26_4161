
import pygame
import myModule  # Import your custom module

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))  # Set display size

# Create a sprite
my_sprite = myModule.makeSprite(50, 50)

# Main loop to display the sprite
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear the screen
    myModule.updateSprite(my_sprite, 100, 100)  # Update and draw your sprite
    pygame.display.flip()  # Update the display

pygame.quit()

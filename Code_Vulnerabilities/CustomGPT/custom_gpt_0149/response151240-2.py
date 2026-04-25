
import pygame
import myModule  # Import your custom module

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create a sprite using your module function
my_sprite = myModule.make_sprite((255, 0, 0), None)  # Red sprite

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Example position
    myModule.update_sprite(my_sprite, (100, 100))

    pygame.display.flip()  # Update the display

pygame.quit()

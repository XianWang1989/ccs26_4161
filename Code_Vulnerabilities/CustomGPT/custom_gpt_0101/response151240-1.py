
# myModule.py
import pygame

def makeSprite():
    # Using pygame to create a sprite
    sprite = pygame.Surface((50, 50))
    sprite.fill((255, 0, 0))  # Fill with red color
    return sprite

def updateSprite(sprite):
    # Example update function
    sprite.fill((0, 255, 0))  # Change color to green
    return sprite

# main_program.py
import pygame
import myModule

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Create a sprite using the module
sprite = myModule.makeSprite()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw the sprite
    sprite = myModule.updateSprite(sprite)
    screen.blit(sprite, (100, 100))
    pygame.display.flip()

pygame.quit()

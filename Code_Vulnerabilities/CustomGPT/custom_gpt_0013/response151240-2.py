
import pygame
import myModule

# Initialize pygame
pygame.init()

# Create a sprite
sprite = myModule.makeSprite(50, 50)

# Update sprite position
sprite_rect = myModule.updateSprite(sprite, (100, 100))

# Setting up display
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))  # Fill with white background
screen.blit(sprite, sprite_rect.topleft)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()


# main_program.py
import pygame
import myModule

pygame.init()

# Create a sprite
sprite = myModule.makeSprite(50, 50)  # Create a 50x50 sprite

# Update sprite position
sprite_rect = myModule.updateSprite(sprite, (100, 100))

# Main loop (simplified)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Drawing (this is just an example context)
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))  # Clear screen with black
    screen.blit(sprite, sprite_rect.topleft)  # Draw the sprite
    pygame.display.flip()

pygame.quit()

import pygame
import myModule

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

sprite = myModule.makeSprite(100, 100)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    myModule.updateSprite(sprite, 1, 0)

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), sprite)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

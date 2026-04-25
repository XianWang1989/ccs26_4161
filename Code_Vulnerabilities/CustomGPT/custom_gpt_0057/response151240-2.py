
import pygame
import myModule

pygame.init()

sprite = myModule.makeSprite(50, 50)
myModule.updateSprite(sprite)
pygame.display.set_mode((800, 600))
pygame.display.get_surface().blit(sprite, (100, 100))
pygame.display.flip()

# Example of using another Pygame function
pygame.time.delay(3000)
pygame.quit()

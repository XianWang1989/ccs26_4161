
import pygame
import sys

def main():
    pygame.init()
    screen_size = (2560, 1440)
    main_surface = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Centering Image Example")

    image_path = 'your_image.png'
    picture = pygame.image.load(image_path)
    size = picture.get_size()

    scale = aspect_scale(size)
    picture = pygame.transform.scale(picture, scale)

    picture_rect = picture.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        main_surface.fill((0, 0, 0))
        main_surface.blit(picture, picture_rect.topleft)
        pygame.display.update()

def aspect_scale(size):
    max_dim = max(size)
    scale = 400  # adjust this scaling factor as necessary
    return (int(size[0] * scale / max_dim), int(size[1] * scale / max_dim))

if __name__ == "__main__":
    main()

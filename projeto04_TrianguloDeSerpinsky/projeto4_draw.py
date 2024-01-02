from projeto04 import *
import pygame

pygame.init()

FPS = 60
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SIERPINSKI TRIANGLE')

STEP = 100


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill((255, 255, 255))

        for y in range(WIDTH // STEP):
            for x in range(HEIGHT // STEP):
                if x <= y:
                    ###output_to_file(f'{y,x}, {COMBINATION(y,x)}')
                    if COMBINATION(y, x) % 2 == 0:
                        pygame.draw.rect(WIN, (0, 0, 0), (x * STEP, y * STEP, STEP, STEP))
                    else:
                        pygame.draw.rect(WIN, (255, 255, 255), (x * STEP, y * STEP, STEP, STEP))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


main()

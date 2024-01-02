from PARTICLES import *


pygame.init()
pygame.display.set_caption('TESTE')


def main():
    run = True
    clock = pygame.time.Clock()

    p1 = Particle(100, 100, 1, 0, 100)
    p2 = Particle(600, 100, 0, 0, 1)
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill((255, 255, 255))

        #PARTICLES MOTION
        p1.update()
        p1.show()
        p1.boundaryCollision()
        p1.particleCollision(p2)

        p2.update()
        p2.show()
        p2.boundaryCollision()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


main()

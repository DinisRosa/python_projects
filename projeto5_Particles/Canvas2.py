from PARTICLES import *


pygame.init()
pygame.display.set_caption('PARTICLES MOTION')


def main():
    run = True
    clock = pygame.time.Clock()

    particles = []
    for i in range(50):
        particles.append(Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT), random.randint(-300, 300), random.randint(-300, 300), random.randint(1, 100),))

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill((255, 255, 255))

        #PARTICLES MOTION
        for p in particles:
            p.show()
            p.update()
            p.boundaryCollision()
            for i in particles:
                if i is not p:
                    p.particleCollision(i)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


main()

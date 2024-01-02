import random
import math
import pygame


WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FPS = 120
dt = 1 / FPS
FRICTION = .9


class Particle:
    def __init__(self, x, y, x_vel, y_vel, mass):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.vel = math.sqrt(math.pow(self.x_vel, 2) + math.pow(self.y_vel, 2))
        if self.x_vel == 0:
            self.angle = 90
        else:
            self.angle = math.atan(self.y_vel / self.x_vel)

        self.mass = mass
        self.radius = 5

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.path = []

    def show(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.x_vel * dt
        self.y += self.y_vel * dt
        self.path.append((self.x, self.y))

    def boundaryCollision(self):
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.x_vel *= -1
        if self.x + self.radius >= WIDTH:
            self.x = WIDTH - self.radius
            self.x_vel *= -1
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.y_vel *= -1
        if self.y + self.radius >= HEIGHT:
            self.y = HEIGHT - self.radius
            self.y_vel *= -1

    def particleCollision(self, other):
        if math.pow((self.x - other.x), 2) + math.pow((self.y - other.y), 2) <= math.pow((self.radius + other.radius), 2):
            totalMass = self.mass + other.mass
            new_x_Vel = (self.mass - other.mass) / totalMass * self.x_vel + (2 * other.mass / totalMass) * other.x_vel
            new_y_Vel = (self.mass - other.mass) / totalMass * self.y_vel + (2 * other.mass / totalMass) * other.y_vel

            other_new_x_vel = -1 * (self.mass - other.mass) / totalMass * other.x_vel + (2 * self.mass / totalMass) * self.x_vel
            other_new_y_vel = -1 * (self.mass - other.mass) / totalMass * other.y_vel + (2 * self.mass / totalMass) * self.y_vel

            self.x_vel = new_x_Vel * FRICTION
            self.y_vel = new_y_Vel * FRICTION

            other.x_vel = other_new_x_vel * FRICTION
            other.y_vel = other_new_y_vel * FRICTION

    def drawPath(self):
        if len(self.path) > 2:
            pygame.draw.lines(WIN, self.color, False, self.path, 2)
        if len(self.path) > 10000:
            self.path.pop(0)



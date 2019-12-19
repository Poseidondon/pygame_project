import pygame
import random
import math


class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, radius, dir=None, speed=None, vx=None, vy=None):
        super().__init__(all_sprites)
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0] - radius, pos[1] - radius
        self.clock = pygame.time.Clock()
        pygame.draw.circle(self.image, (255, 100, 0), (radius, radius), radius)

        self.float_pos = self.float_x, self.float_y = pos[0], pos[1]
        self.radius = radius
        if dir and speed:
            self.dir = dir
            dir = (dir + 90) % 360
            self.vx = (math.cos(math.radians(dir)) * speed)
            self.vy = math.sin(math.radians(dir)) * speed
            self.speed = math.hypot(self.vx, self.vy)
        elif vx and vy:
            self.vx = vx
            self.vy = vy
            self.speed = math.hypot(self.vx, self.vy)
        else:
            print('Particle error!')

    def update(self):
        time = self.clock.tick() / 1000

        self.float_x += self.vx * time
        self.float_y -= self.vy * time
        self.rect.x = self.float_x
        self.rect.y = self.float_y


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(all_sprites)
        self.radius = radius
        self.clock = pygame.time.Clock()
        self.k = 1.4
        self.image = pygame.Surface((2 * radius * self.k, 2 * radius * self.k), pygame.SRCALPHA, 32)
        self.rect = self.image.get_rect()
        self.setDir(0)

        self.particle_point = (0, 0)
        self.float_pos = self.float_x, self.float_y = x, y
        self.vx = self.vy = 0
        self.speed = 0
        self.accelerate = 0
        self.rot_speed = 0
        self.dir = 0

        self.forward_accelerate = 150
        self.backward_accelerate = -50
        self.max_rot_speed = 180
        self.max_speed = 250
        self.friction = 8

    def setDir(self, angle):
        self.image.fill(pygame.SRCALPHA)
        angle = (angle - 90) % 360
        r = self.radius * 0.6
        points_1 = [(self.radius * self.k + math.cos(math.radians(angle)) * self.radius * self.k,
                     self.radius * self.k + math.sin(math.radians(angle)) * self.radius * self.k),
                    (self.radius * self.k + math.cos(math.radians(angle + 150)) * self.radius * self.k,
                     self.radius * self.k + math.sin(math.radians(angle + 150)) * self.radius * self.k),
                    (self.radius * self.k + math.cos(math.radians(angle - 150)) * self.radius * self.k,
                     self.radius * self.k + math.sin(math.radians(angle - 150)) * self.radius * self.k)]
        points_2 = [(self.radius * self.k + math.cos(math.radians(angle)) * r,
                     self.radius * self.k + math.sin(math.radians(angle)) * r),
                    (self.radius * self.k + math.cos(math.radians(angle + 150)) * r,
                     self.radius * self.k + math.sin(math.radians(angle + 150)) * r),
                    (self.radius * self.k + math.cos(math.radians(angle - 150)) * r,
                     self.radius * self.k + math.sin(math.radians(angle - 150)) * r)]
        pygame.draw.polygon(self.image, (100, 0, 0), points_1)
        pygame.draw.polygon(self.image, (255, 0, 0), points_2)
        pygame.draw.circle(self.image, (0, 255, 0),
                           (int(self.radius * self.k), int(self.radius * self.k)), self.radius, 1)
        self.particle_point = (self.radius * self.k + math.cos(math.radians((angle + 180) % 360)) * self.radius,
                               self.radius * self.k + math.sin(math.radians((angle + 180) % 360)) * self.radius)

    def addVector(self, force, dir=None):
        if not dir:
            dir = self.dir

        dir = (dir + 90) % 360
        self.vx -= math.cos(math.radians(dir)) * force
        self.vy += math.sin(math.radians(dir)) * force
        self.speed = math.hypot(self.vx, self.vy)

    def update(self):
        time = self.clock.tick() / 1000
        if self.rot_speed:
            self.dir = (self.dir + self.rot_speed * time) % 360
            self.setDir(self.dir)
        if self.accelerate:
            self.addVector(self.accelerate * time, self.dir)
        else:
            if self.speed < 3:
                self.speed = self.vx = self.vy = 0

        if self.friction:
            friction = self.friction * time
            if friction < self.speed:
                k = (self.speed - friction) / self.speed
                self.speed -= friction
                self.vx *= k
                self.vy *= k
            else:
                self.speed = self.vx = self.vy = 0
        if self.max_speed and self.speed > self.max_speed:
            k = self.max_speed / self.speed
            self.speed = self.max_speed
            self.vx *= k
            self.vy *= k

        self.float_x += self.vx * time
        self.float_y -= self.vy * time
        self.rect.x = self.float_x
        self.rect.y = self.float_y

        Particle(pos=(self.particle_point[0] + self.rect.x, self.particle_point[1] + self.rect.y),
                 radius=random.randint(1, 5), dir=(self.dir + 180) % 360, speed=30)


pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()

player = Player(400, 300, 16)

running = True

while running:
    screen.fill((155, 155, 155))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == 273:
                player.accelerate = player.forward_accelerate
            if event.key == 274:
                player.accelerate = player.backward_accelerate
            if event.key == 275:
                player.rot_speed = player.max_rot_speed
            if event.key == 276:
                player.rot_speed = -player.max_rot_speed

        if event.type == pygame.KEYUP:
            if event.key == 273 and player.accelerate > 0:
                player.accelerate = 0
            if event.key == 274 and player.accelerate < 0:
                player.accelerate = 0
            if event.key == 275 and player.rot_speed > 0:
                player.rot_speed = 0
            if event.key == 276 and player.rot_speed < 0:
                player.rot_speed = 0

    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()

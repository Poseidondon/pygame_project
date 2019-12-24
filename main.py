import pygame
import random
import math


class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, radius, dir=None, speed=None):
        super().__init__(all_sprites)

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0] - radius, pos[1] - radius
        self.float_pos = self.float_x, self.float_y = pos[0], pos[1]
        self.radius = radius

        self.clock = pygame.time.Clock()
        self.spawn_time = pygame.time.get_ticks()
        self.alpha = 255
        self.lifetime = 0

        self.max_lifetime = None
        self.increase = None
        self.max_size = None
        self.gradient_k = 3

        self.dir = dir
        dir = (dir + 90) % 360
        self.vx = -(math.cos(math.radians(dir)) * speed)
        self.vy = math.sin(math.radians(dir)) * speed
        self.speed = math.hypot(self.vx, self.vy)

    def set_max_lifetime(self, max_lifetime):
        self.max_lifetime = max_lifetime

    def set_increase(self, increase):
        self.increase = increase

    def set_max_size(self, max_size):
        self.max_size = max_size

    def set_gradient(self, color_1, color_2):
        self.color_1 = color_1
        self.color_2 = color_2

    def set_gradient_k(self, gradient_k):
        self.gradient_k = gradient_k

    def get_color(self):
        if self.color_1 != self.color_2:
            if self.lifetime > self.max_lifetime / self.gradient_k:
                return self.color_2
            else:
                r = self.color_1[0] +\
                    (self.color_2[0] - self.color_1[0]) * (self.lifetime / (self.max_lifetime / self.gradient_k))
                g = self.color_1[1] +\
                    (self.color_2[1] - self.color_1[1]) * (self.lifetime / (self.max_lifetime / self.gradient_k))
                b = self.color_1[2] +\
                    (self.color_2[2] - self.color_1[2]) * (self.lifetime / (self.max_lifetime / self.gradient_k))
                return r, g, b
        else:
            return self.color_1

    def update(self):
        time = self.clock.tick() / 1000
        self.lifetime = pygame.time.get_ticks() - self.spawn_time

        if self.increase:
            self.radius += self.increase * time
            self.image = pygame.Surface((2 * int(self.radius), 2 * int(self.radius)), pygame.SRCALPHA)
            self.rect = self.image.get_rect()

        if self.max_lifetime:
            self.alpha = (self.max_lifetime - self.lifetime) / self.max_lifetime * 255
            self.alpha = max(0, self.alpha)

        c = self.get_color()
        pygame.draw.circle(self.image, (c[0], c[1], c[2], int(self.alpha)),
                           (int(self.radius), int(self.radius)), int(self.radius))

        self.float_x += self.vx * time
        self.float_y -= self.vy * time
        self.rect.x = self.float_x - self.radius
        self.rect.y = self.float_y - self.radius

        if not (self.rect.x in range(-int(self.radius), width + int(self.radius))
                and self.rect.y in range(-int(self.radius), height + int(self.radius))):
            self.kill()
        if self.max_lifetime:
            if self.lifetime >= self.max_lifetime:
                self.kill()
        if self.max_size:
            if self.radius >= self.max_size:
                self.kill()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, collider=False):
        super().__init__(all_sprites)
        self.radius = radius
        self.clock = pygame.time.Clock()
        self.collider = collider
        self.k = 1.4
        self.image = pygame.Surface((2 * radius * self.k, 2 * radius * self.k), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.particle_point = (0, 0)
        self.setDir(0)

        self.float_pos = self.float_x, self.float_y = x, y
        self.vx = self.vy = 0
        self.speed = 0
        self.accelerate = 0
        self.rot_speed = 0
        self.dir = 0

        self.particle_spawner = 0

        self.forward_accelerate = 250
        self.backward_accelerate = -50
        self.max_rot_speed = 180
        self.max_speed = 250
        self.friction = 8
        self.particles_pers = 50

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
        if self.collider:
            pygame.draw.circle(self.image, (0, 255, 0),
                               (int(self.radius * self.k), int(self.radius * self.k)), self.radius, 1)
        self.particle_point = (
            self.radius * self.k + math.cos(math.radians((angle + 180) % 360)) * self.radius * self.k,
            self.radius * self.k + math.sin(math.radians((angle + 180) % 360)) * self.radius * self.k)

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
            if self.accelerate > 0:
                self.particle_spawner += time * self.particles_pers
                for _ in range(int(self.particle_spawner)):
                    spreading = 90
                    angle = random.randint(-spreading / 2, spreading / 2)
                    p = Particle(pos=(self.particle_point[0] + self.rect.x, self.particle_point[1] + self.rect.y),
                                 radius=7, dir=(self.dir + 180 + angle) % 360, speed=100)
                    p.set_gradient((255, 162, 0), (0, 0, 0))
                    p.set_gradient_k(2)
                    p.set_increase(30)
                    p.set_max_lifetime(500)
                    p.set_max_size(None)
                self.particle_spawner -= int(self.particle_spawner)

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


def show_fps():
    fps = FPS_FONT.render(f'FPS: {int(clock.get_fps())}', 1, (0, 0, 0))
    screen.blit(fps, (width - fps.get_width() - 5, 10))


pygame.init()
size = width, height = (1024, 768)
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()

clock = pygame.time.Clock()
FPS_FONT = pygame.font.Font(None, 18)

player = Player(400, 300, 16)

running = True

while running:
    screen.fill((255, 255, 255))
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
    show_fps()
    clock.tick()
    pygame.display.flip()

pygame.quit()

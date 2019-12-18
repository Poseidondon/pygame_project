import pygame
import random
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(all_sprites)
        self.radius = radius
        self.clock = pygame.time.Clock()
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.setDir(0)

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
        points_1 = [(self.radius + math.cos(math.radians(angle)) * self.radius,
                     self.radius + math.sin(math.radians(angle)) * self.radius),
                    (self.radius + math.cos(math.radians(angle + 150)) * self.radius,
                     self.radius + math.sin(math.radians(angle + 150)) * self.radius),
                    (self.radius + math.cos(math.radians(angle - 150)) * self.radius,
                     self.radius + math.sin(math.radians(angle - 150)) * self.radius)]
        points_2 = [(self.radius + math.cos(math.radians(angle)) * r,
                     self.radius + math.sin(math.radians(angle)) * r),
                    (self.radius + math.cos(math.radians(angle + 150)) * r,
                     self.radius + math.sin(math.radians(angle + 150)) * r),
                    (self.radius + math.cos(math.radians(angle - 150)) * r,
                     self.radius + math.sin(math.radians(angle - 150)) * r)]
        pygame.draw.polygon(self.image, (100, 0, 0), points_1)
        pygame.draw.polygon(self.image, (255, 0, 0), points_2)

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

import os
import pygame
import random
import math


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = pygame.image.load(fullname).convert_alpha()
    return image


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__(all_sprites)
        self.radius = radius
        self.clock = pygame.time.Clock()
        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x - radius // 2, y - radius // 2, radius * 2, radius * 2)
        self.setDir(0)

        self.vx = self.vy = 0
        self.speed = 0
        self.accelerate = 0
        self.rot_speed = 0
        self.dir = 0

        self.max_rot_speed = 180
        self.max_accelerate = 50
        self.max_speed = 500

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

        pass

    def update(self):
        time = self.clock.tick() / 1000
        if self.rot_speed:
            self.dir = (self.dir + self.rot_speed * time) % 360
            self.setDir(self.dir)
        if self.accelerate:
            self.addVector(self.accelerate * time, self.dir)
        self.rect = self.rect.move(self.vx, self.vy)


pygame.init()
size = width, height = (800, 600)
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()

player = Player(400, 300, 16)

running = True

while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == 273:
                player.accelerate = player.max_accelerate
            if event.key == 274:
                player.accelerate = -player.max_accelerate
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

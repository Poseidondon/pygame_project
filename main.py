import pygame
import random
import math


def draw_sprite1(image, radius, angle, color_1, color_2, k=1.5):
    points_1 = ((radius * k + math.cos(math.radians(angle + 100)) * radius * k * 0.35,
                 radius * k + math.sin(math.radians(angle + 100)) * radius * k * 0.35),
                (radius * k + math.cos(math.radians(angle - 100)) * radius * k * 0.35,
                 radius * k + math.sin(math.radians(angle - 100)) * radius * k * 0.35),
                (radius * k + math.cos(math.radians(angle + 180)) * radius * k,
                 radius * k + math.sin(math.radians(angle + 180)) * radius * k))

    points_2 = ((radius * k + math.cos(math.radians(angle)) * radius * k,
                 radius * k + math.sin(math.radians(angle)) * radius * k),
                (radius * k + math.cos(math.radians(angle + 140)) * radius * k,
                 radius * k + math.sin(math.radians(angle + 140)) * radius * k),
                (radius * k, radius * k),
                (radius * k + math.cos(math.radians(angle - 140)) * radius * k,
                 radius * k + math.sin(math.radians(angle - 140)) * radius * k))

    pygame.draw.polygon(image, color_2, points_1)
    pygame.draw.polygon(image, (0, 0, 0), points_1, 2)

    pygame.draw.polygon(image, color_1, points_2)
    pygame.draw.polygon(image, (0, 0, 0), points_2, 2)


def draw_sprite2(image, radius, angle, color_1, color_2, k=1.5):
    points_1 = ((radius * k + math.cos(math.radians(angle)) * radius * k,
                 radius * k + math.sin(math.radians(angle)) * radius * k),
                (radius * k + math.cos(math.radians(angle + 120)) * radius * k * 0.6,
                 radius * k + math.sin(math.radians(angle + 120)) * radius * k * 0.6),
                (radius * k + math.cos(math.radians(angle + 180)) * radius * k * 0.8,
                 radius * k + math.sin(math.radians(angle + 180)) * radius * k * 0.8),
                (radius * k + math.cos(math.radians(angle - 120)) * radius * k * 0.6,
                 radius * k + math.sin(math.radians(angle - 120)) * radius * k * 0.6))

    circle_1 = (int(radius * k + math.cos(math.radians(angle + 180)) * radius * k * 0.25),
                int(radius * k + math.sin(math.radians(angle + 180)) * radius * k * 0.25))
    circle_2 = (int(radius * k + math.cos(math.radians(angle)) * radius * k * 0.25),
                int(radius * k + math.sin(math.radians(angle)) * radius * k * 0.25))

    pygame.draw.polygon(image, color_1, points_1)
    pygame.draw.polygon(image, (0, 0, 0), points_1, 2)

    pygame.draw.circle(image, color_2, circle_1, int(radius * k * 0.3))
    pygame.draw.circle(image, (0, 0, 0), circle_1, int(radius * k * 0.3) + 1, 1)

    pygame.draw.circle(image, color_2, circle_2, int(radius * k * 0.2))
    pygame.draw.circle(image, (0, 0, 0), circle_2, int(radius * k * 0.2) + 1, 1)


def draw_sprite3(image, radius, angle, color_1, color_2, k=1.5):
    points_1 = ((radius * k + math.cos(math.radians(angle)) * radius * k,
                 radius * k + math.sin(math.radians(angle)) * radius * k),
                (radius * k + math.cos(math.radians(angle - 60)) * radius * k * 0.7,
                 radius * k + math.sin(math.radians(angle - 60)) * radius * k * 0.7),
                (radius * k + math.cos(math.radians(angle)) * radius * k * 0.5,
                 radius * k + math.sin(math.radians(angle)) * radius * k * 0.5),
                (radius * k + math.cos(math.radians(angle + 60)) * radius * k * 0.7,
                 radius * k + math.sin(math.radians(angle + 60)) * radius * k * 0.7))

    points_2 = ((radius * k + math.cos(math.radians(angle)) * radius * k * 0.7,
                 radius * k + math.sin(math.radians(angle)) * radius * k * 0.7),
                (radius * k + math.cos(math.radians(angle - 90)) * radius * k * 0.7,
                 radius * k + math.sin(math.radians(angle - 90)) * radius * k * 0.7),
                (radius * k + math.cos(math.radians(angle)) * radius * k * 0.25,
                 radius * k + math.sin(math.radians(angle)) * radius * k * 0.25),
                (radius * k + math.cos(math.radians(angle + 90)) * radius * k * 0.7,
                 radius * k + math.sin(math.radians(angle + 90)) * radius * k * 0.7))

    points_3 = ((radius * k + math.cos(math.radians(angle)) * radius * k * 0.4,
                 radius * k + math.sin(math.radians(angle)) * radius * k * 0.4),
                (radius * k + math.cos(math.radians(angle - 110)) * radius * k * 0.7,
                 radius * k + math.sin(math.radians(angle - 110)) * radius * k * 0.7),
                (radius * k + math.cos(math.radians(angle + 180)) * radius * k * 0.1,
                 radius * k + math.sin(math.radians(angle + 180)) * radius * k * 0.1),
                (radius * k + math.cos(math.radians(angle + 110)) * radius * k * 0.7,
                 radius * k + math.sin(math.radians(angle + 110)) * radius * k * 0.7))

    points_4 = ((radius * k, radius * k),
                (radius * k + math.cos(math.radians(angle - 130)) * radius * k * 0.8,
                 radius * k + math.sin(math.radians(angle - 130)) * radius * k * 0.8),
                (radius * k + math.cos(math.radians(angle + 180)) * radius * k * 0.4,
                 radius * k + math.sin(math.radians(angle + 180)) * radius * k * 0.4),
                (radius * k + math.cos(math.radians(angle + 130)) * radius * k * 0.8,
                 radius * k + math.sin(math.radians(angle + 130)) * radius * k * 0.8))

    pygame.draw.polygon(image, color_2, points_4)
    pygame.draw.polygon(image, (0, 0, 0), points_4, 2)

    pygame.draw.polygon(image, color_1, points_3)
    pygame.draw.polygon(image, (0, 0, 0), points_3, 2)

    pygame.draw.polygon(image, color_2, points_2)
    pygame.draw.polygon(image, (0, 0, 0), points_2, 2)

    pygame.draw.polygon(image, color_1, points_1)
    pygame.draw.polygon(image, (0, 0, 0), points_1, 2)


def draw_sprite4(image, radius, angle, color_1, color_2, k=1.5):
    points_1 = ((radius * k + math.cos(math.radians(angle + 30)) * radius * k,
                 radius * k + math.sin(math.radians(angle + 30)) * radius * k),
                (radius * k + math.cos(math.radians(angle - 165)) * radius * k,
                 radius * k + math.sin(math.radians(angle - 165)) * radius * k),
                (radius * k + math.cos(math.radians(angle - 30)) * radius * k,
                 radius * k + math.sin(math.radians(angle - 30)) * radius * k),
                (radius * k + math.cos(math.radians(angle + 165)) * radius * k,
                 radius * k + math.sin(math.radians(angle + 165)) * radius * k))

    points_2 = ((radius * k + math.cos(math.radians(angle)) * radius * k,
                 radius * k + math.sin(math.radians(angle)) * radius * k),
                (radius * k + math.cos(math.radians(angle - 140)) * radius * k * 0.5,
                 radius * k + math.sin(math.radians(angle - 140)) * radius * k * 0.5),
                (radius * k + math.cos(math.radians(angle + 140)) * radius * k * 0.5,
                 radius * k + math.sin(math.radians(angle + 140)) * radius * k * 0.5))

    pygame.draw.polygon(image, color_1, points_2)
    pygame.draw.polygon(image, (0, 0, 0), points_2, 2)

    pygame.draw.polygon(image, color_2, points_1)
    pygame.draw.polygon(image, (0, 0, 0), points_1, 2)


CARS = [draw_sprite1, draw_sprite2, draw_sprite3, draw_sprite4]
# Preset: (f_acc, b_acc, rot_speed, speed, particles_per, particles_par, sprite_index, health)
# Particles: [gradient:gradient_k:increase:max_lifetime:max_size:spreading:speed_k]
CAR_PRESETS = {'beginner': (180, -50, 100, 180, 50, '(255, 162, 0), (0, 0, 0):2:30:500:None:90:1', 1, 1500),
               'medium': (200, -50, 150, 250, 200, '(0, 245, 255), (255, 255, 255):1:30:100:None:100:5', 3, 2000),
               'advanced': (250, -50, 180, 280, 50, '(13, 150, 0), (0, 0, 0):1:30:1500:None:180:0.5', 2, 2000),
               'pro': (320, -50, 250, 350, 100, '(255, 255, 255), (0, 0, 0):1.5:30:900:None:30:5', 0, 1000)}

CUR_CAR = CAR_PRESETS['pro']


def angleTo(point2, point1):
    radius = math.hypot(point1[0] - point2[0], point1[1] - point2[1])
    if radius == 0:
        return 0
    angle = math.degrees(math.acos((point2[0] - point1[0]) / radius))
    if point2[1] < point1[1]:
        angle = 360 - angle
    angle = (angle - 90) % 360
    return angle


class Border(pygame.sprite.Sprite):
    def __init__(self, pos1, pos2, visible=False):
        super().__init__(all_sprites)
        self.add(borders)
        thickness = 1
        self.pos1 = x1, y1 = pos1
        self.pos2 = x2, y2 = pos2
        if x2 < x1:
            x1, x2 = x2, x1
        if y2 < y1:
            y1, y2 = y2, y1
        self.image = pygame.Surface((x2 - x1 + thickness, y2 - y1 + thickness), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x1, y1, x2 - x1 + thickness, y2 - y1 + thickness)
        if visible:
            pygame.draw.line(self.image, (0, 255, 0),
                             (pos1[0] - x1, pos1[1] - y1), (x2 - pos1[0], y2 - pos1[1]), thickness)


class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, radius, dir=None, speed=None):
        super().__init__(all_sprites)

        self.image = pygame.Surface((2 * radius, 2 * radius), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0] - radius, pos[1] - radius
        self.float_pos = self.float_x, self.float_y = pos[0], pos[1]
        self.radius = radius

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
                r = self.color_1[0] + \
                    (self.color_2[0] - self.color_1[0]) * (self.lifetime / (self.max_lifetime / self.gradient_k))
                g = self.color_1[1] + \
                    (self.color_2[1] - self.color_1[1]) * (self.lifetime / (self.max_lifetime / self.gradient_k))
                b = self.color_1[2] + \
                    (self.color_2[2] - self.color_1[2]) * (self.lifetime / (self.max_lifetime / self.gradient_k))
                return r, g, b
        else:
            return self.color_1

    def apply_pars(self, pars):
        self.set_gradient(pars[0][0], pars[0][1])
        self.set_gradient_k(pars[1])
        self.set_increase(pars[2])
        self.set_max_lifetime(pars[3])
        self.set_max_size(pars[4])

    def update(self):
        self.lifetime = pygame.time.get_ticks() - self.spawn_time

        if self.increase:
            self.radius += self.increase * TIME
            self.image = pygame.Surface((2 * int(self.radius), 2 * int(self.radius)), pygame.SRCALPHA)
            self.rect = self.image.get_rect()

        if self.max_lifetime:
            self.alpha = (self.max_lifetime - self.lifetime) / self.max_lifetime * 255
            self.alpha = max(0, self.alpha)

        c = self.get_color()
        pygame.draw.circle(self.image, (c[0], c[1], c[2], int(self.alpha)),
                           (int(self.radius), int(self.radius)), int(self.radius))

        self.float_x += self.vx * TIME
        self.float_y -= self.vy * TIME
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
    def __init__(self, x, y, radius, collider=False, preset=CAR_PRESETS['beginner']):
        super().__init__(all_sprites)
        self.radius = radius
        self.collider = collider
        self.k = 1.4
        self.image = pygame.Surface((2 * radius * self.k, 2 * radius * self.k), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.particle_point = (0, 0)

        self.float_pos = self.float_x, self.float_y = x, y
        self.vx = self.vy = 0
        self.speed = 0
        self.accelerate = 0
        self.rot_speed = 0
        self.dir = 0

        self.particle_spawner = 0

        self.applyPreset(preset)
        self.spreading = self.partciles_par[5]
        self.speed_k = self.partciles_par[6]
        self.friction = 20

        self.setDir(0)

    def drawHealth(self):
        health_mes = pygame.font.Font(None, 32).render('Health:', 1, (0, 0, 0))
        screen.blit(health_mes, (5, height - health_mes.get_height() - 30))
        if self.health > 0:
            k = self.health / self.max_health
            color = (255 * (1 - k), 255 * k, 0)
            pygame.draw.rect(screen, color, (5, height - 25, int(200 * k), 20))
        pygame.draw.rect(screen, (0, 0, 0), (5, height - 25, 200, 20), 2)

    def death(self):
        print('death')

    def applyPreset(self, preset):
        self.forward_accelerate = preset[0]
        self.backward_accelerate = preset[1]
        self.max_rot_speed = preset[2]
        self.max_speed = preset[3]
        self.particles_pers = preset[4]
        self.partciles_par = [eval(i) for i in preset[5].split(':')]
        self.draw = CARS[preset[6]]
        self.health = preset[7]
        self.max_health = self.health

    def setDir(self, angle):
        self.image.fill(pygame.SRCALPHA)
        angle = (angle - 90) % 360
        self.draw(self.image, self.radius, angle, (128, 0, 0), (128, 128, 0), k=self.k)

        if self.collider:
            pygame.draw.circle(self.image, (0, 255, 0),
                               (int(self.radius * self.k), int(self.radius * self.k)), self.radius, 1)

        self.particle_point = (
            self.radius * self.k + math.cos(math.radians((angle + 180) % 360)) * self.radius * self.k * 0.9,
            self.radius * self.k + math.sin(math.radians((angle + 180) % 360)) * self.radius * self.k * 0.9)

    def moveDir(self):
        return angleTo((self.float_x, self.float_y), (self.float_x + self.vx, self.float_y - self.vy))

    def addVector(self, force, dir=None):
        if not dir:
            dir = self.dir

        dir = (dir + 90) % 360
        self.vx -= math.cos(math.radians(dir)) * force
        self.vy += math.sin(math.radians(dir)) * force
        self.speed = math.hypot(self.vx, self.vy)

    def setVector(self, force, dir=None):
        if not dir:
            dir = self.dir

        dir = (dir + 90) % 360
        self.vx = -math.cos(math.radians(dir)) * force
        self.vy = math.sin(math.radians(dir)) * force
        self.speed = math.hypot(self.vx, self.vy)

    def borderDist(self, point1, border):
        point2, point3 = border.pos1, border.pos2
        p1_2Angle = angleTo(point1, point2)
        p2_xAngle = angleTo(point3, point2)
        p1_p2 = math.hypot(point1[0] - point2[0], point1[1] - point2[1])
        p2_x = math.cos(math.radians(math.fabs(p1_2Angle - p2_xAngle))) * p1_p2
        x = point2[0] + math.sin(math.radians((p2_xAngle + 180) % 360)) * p2_x
        y = point2[1] + math.cos(math.radians(p2_xAngle)) * p2_x
        if x < min(point2[0], point3[0]):
            x = min(point2[0], point3[0])
        elif x >= max(point2[0], point3[0]):
            x = max(point2[0], point3[0])
        if y < min(point2[1], point3[1]):
            y = min(point2[1], point3[1])
        elif y >= max(point2[1], point3[1]):
            y = max(point2[1], point3[1])
        return math.hypot(point1[0] - x, point1[1] - y), (x, y)

    def update(self):
        if self.rot_speed:
            self.dir = (self.dir + self.rot_speed * TIME) % 360
            self.setDir(self.dir)

        if self.accelerate:
            self.addVector(self.accelerate * TIME, self.dir)
            if self.accelerate > 0:
                self.particle_spawner += TIME * self.particles_pers
                for _ in range(int(self.particle_spawner)):
                    angle = random.randint(-self.spreading / 2, self.spreading / 2)
                    p = Particle(pos=(self.particle_point[0] + self.rect.x, self.particle_point[1] + self.rect.y),
                                 radius=7, dir=(self.dir + 180 + angle) % 360, speed=int(100 * self.speed_k))
                    p.apply_pars(self.partciles_par)
                self.particle_spawner -= int(self.particle_spawner)
        else:
            if self.speed < 3:
                self.speed = self.vx = self.vy = 0

        for border in borders:
            point1 = self.rect.x + self.radius * self.k, self.rect.y + self.radius * self.k
            dist, pos = self.borderDist(point1, border)
            if dist <= self.radius:
                angleCol = angleTo((point1[0], point1[1]), pos)
                moveDir = self.moveDir()
                angle_betw = moveDir - angleCol
                if angle_betw > 180:
                    angle_betw = -360 + angle_betw
                elif angle_betw < -180:
                    angle_betw = 360 + angle_betw
                if -90 < angle_betw < 90:
                    new_vx = math.cos(math.radians(angle_betw)) * self.speed
                    new_vy = math.sin(math.radians(angle_betw)) * self.speed
                    final_vy = new_vy * 0.99
                    self.setVector(new_vy * 0.99, angleCol + 90)
                    impact = new_vx + math.fabs(new_vy - final_vy)
                    if impact >= 2:
                        self.health -= impact
                        if self.health <= 0:
                            self.death()
        self.drawHealth()

        if self.friction:
            friction = self.friction * TIME
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

        self.float_x += self.vx * TIME
        self.float_y -= self.vy * TIME
        self.rect.x = self.float_x
        self.rect.y = self.float_y


def show_fps():
    fps = pygame.font.Font(None, 18).render(f'FPS: {int(CLOCK.get_fps())}', 1, (0, 0, 0))
    screen.blit(fps, (width - fps.get_width() - 5, 10))


pygame.init()
size = width, height = (1024, 768)
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
borders = pygame.sprite.Group()

CLOCK = pygame.time.Clock()

player = Player(400, 300, 16, preset=CUR_CAR, collider=True)
Border((100, 100), (250, 250), visible=True)
Border((300, 300), (300, 600), visible=True)
Border((500, 500), (200, 500), visible=True)

running = True

while running:
    screen.fill((127, 127, 127))
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

    show_fps()
    TIME = CLOCK.tick() / 1000
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.flip()

pygame.quit()

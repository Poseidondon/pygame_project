import pygame
import random
import math
import sys
import os

pygame.init()
pygame.display.set_caption('Arrow Racer')
size = width, height = (1024, 768)
screen = pygame.display.set_mode(size)

MEDIUM_PRICE = 100
ADVANCED_PRICE = 200
PRO_PRICE = 400
LEVEL_MONEY = 200


def nothing():
    pass


def terminate():
    save_data()
    pygame.quit()
    sys.exit()


# Загрузка уровня
def load_level(name):
    f = open('levels/' + name, 'r', encoding='utf-8')
    borders, checkpoints, laps, k, time = [eval(i) for i in f.readlines()]
    borders = [((i[0][0] * k, i[0][1] * k), (i[1][0] * k, i[1][1] * k)) for i in borders]
    checkpoints = [((i[0][0] * k, i[0][1] * k), (i[1][0] * k, i[1][1] * k)) for i in checkpoints]
    f.close()

    for b in borders:
        Border(b[0], b[1], color=(0, 0, 0))

    checks = []
    c = checkpoints[0]
    checks.append(Checkpoint(c[0], c[1], finish=True))
    for c in checkpoints[1:]:
        checks.append(Checkpoint(c[0], c[1]))

    return Player(0, 0, (COLOR_1, COLOR_2), CUR_CAR, checks, laps), time


# Загрузка данных
def load_data():
    global CUR_CAR, COLOR_1, COLOR_2, BALANCE, BALANCE_MES, UNLOCKED_CARS, RECORDS
    f = open('data.txt', 'r', encoding='utf-8')
    data = [eval(i) for i in f.readlines()]
    f.close()
    CUR_CAR = CAR_PRESETS[data[0]]
    COLOR_1 = data[1]
    COLOR_2 = data[2]
    BALANCE = data[3]
    BALANCE_MES = pygame.font.Font(None, 120).render('$' + str(BALANCE), 1, (20, 180, 0))
    UNLOCKED_CARS = data[4]
    RECORDS = data[5]


# Сохранение данных
def save_data():
    f = open('data.txt', 'w', encoding='utf-8')
    car = "'" + list(CAR_PRESETS.keys())[list(CAR_PRESETS.values()).index(CUR_CAR)] + "'"
    data = '\n'.join([car, str(COLOR_1), str(COLOR_2), str(BALANCE), str(UNLOCKED_CARS), str(RECORDS)])
    f.write(data)
    f.close()


# Функции отрисовки игрока
def draw_sprite1(image, radius, angle, color_1, color_2, k=1.5, shift_x=0, shift_y=0):
    points_1 = ((shift_x + radius * k + math.cos(math.radians(angle + 100)) * radius * k * 0.35,
                 shift_y + radius * k + math.sin(math.radians(angle + 100)) * radius * k * 0.35),
                (shift_x + radius * k, shift_y + radius * k),
                (shift_x + radius * k + math.cos(math.radians(angle - 100)) * radius * k * 0.35,
                 shift_y + radius * k + math.sin(math.radians(angle - 100)) * radius * k * 0.35),
                (shift_x + radius * k + math.cos(math.radians(angle + 180)) * radius * k,
                 shift_y + radius * k + math.sin(math.radians(angle + 180)) * radius * k))

    points_2 = ((shift_x + radius * k + math.cos(math.radians(angle)) * radius * k,
                 shift_y + radius * k + math.sin(math.radians(angle)) * radius * k),
                (shift_x + radius * k + math.cos(math.radians(angle + 140)) * radius * k,
                 shift_y + radius * k + math.sin(math.radians(angle + 140)) * radius * k),
                (shift_x + radius * k, shift_y + radius * k),
                (shift_x + radius * k + math.cos(math.radians(angle - 140)) * radius * k,
                 shift_y + radius * k + math.sin(math.radians(angle - 140)) * radius * k))

    pygame.draw.polygon(image, color_2, points_1)
    pygame.draw.polygon(image, (0, 0, 0), points_1, 2)

    pygame.draw.polygon(image, color_1, points_2)
    pygame.draw.polygon(image, (0, 0, 0), points_2, 2)


def draw_sprite2(image, radius, angle, color_1, color_2, k=1.5, shift_x=0, shift_y=0):
    points_1 = ((shift_x + radius * k + math.cos(math.radians(angle)) * radius * k,
                 shift_y + radius * k + math.sin(math.radians(angle)) * radius * k),
                (shift_x + radius * k + math.cos(math.radians(angle + 120)) * radius * k * 0.6,
                 shift_y + radius * k + math.sin(math.radians(angle + 120)) * radius * k * 0.6),
                (shift_x + radius * k + math.cos(math.radians(angle + 180)) * radius * k * 0.8,
                 shift_y + radius * k + math.sin(math.radians(angle + 180)) * radius * k * 0.8),
                (shift_x + radius * k + math.cos(math.radians(angle - 120)) * radius * k * 0.6,
                 shift_y + radius * k + math.sin(math.radians(angle - 120)) * radius * k * 0.6))

    circle_1 = (int(shift_x + radius * k + math.cos(math.radians(angle + 180)) * radius * k * 0.25),
                int(shift_y + radius * k + math.sin(math.radians(angle + 180)) * radius * k * 0.25))
    circle_2 = (int(shift_x + radius * k + math.cos(math.radians(angle)) * radius * k * 0.25),
                int(shift_y + radius * k + math.sin(math.radians(angle)) * radius * k * 0.25))

    pygame.draw.polygon(image, color_1, points_1)
    pygame.draw.polygon(image, (0, 0, 0), points_1, 2)

    pygame.draw.circle(image, color_2, circle_1, int(radius * k * 0.3))
    pygame.draw.circle(image, (0, 0, 0), circle_1, int(radius * k * 0.3) + 1, 1)

    pygame.draw.circle(image, color_2, circle_2, int(radius * k * 0.2))
    pygame.draw.circle(image, (0, 0, 0), circle_2, int(radius * k * 0.2) + 1, 1)


def draw_sprite3(image, radius, angle, color_1, color_2, k=1.5, shift_x=0, shift_y=0):
    points_1 = ((shift_x + radius * k + math.cos(math.radians(angle)) * radius * k,
                 shift_y + radius * k + math.sin(math.radians(angle)) * radius * k),
                (shift_x + radius * k + math.cos(math.radians(angle - 60)) * radius * k * 0.7,
                 shift_y + radius * k + math.sin(math.radians(angle - 60)) * radius * k * 0.7),
                (shift_x + radius * k + math.cos(math.radians(angle)) * radius * k * 0.5,
                 shift_y + radius * k + math.sin(math.radians(angle)) * radius * k * 0.5),
                (shift_x + radius * k + math.cos(math.radians(angle + 60)) * radius * k * 0.7,
                 shift_y + radius * k + math.sin(math.radians(angle + 60)) * radius * k * 0.7))

    points_2 = ((shift_x + radius * k + math.cos(math.radians(angle)) * radius * k * 0.7,
                 shift_y + radius * k + math.sin(math.radians(angle)) * radius * k * 0.7),
                (shift_x + radius * k + math.cos(math.radians(angle - 90)) * radius * k * 0.7,
                 shift_y + radius * k + math.sin(math.radians(angle - 90)) * radius * k * 0.7),
                (shift_x + radius * k + math.cos(math.radians(angle)) * radius * k * 0.25,
                 shift_y + radius * k + math.sin(math.radians(angle)) * radius * k * 0.25),
                (shift_x + radius * k + math.cos(math.radians(angle + 90)) * radius * k * 0.7,
                 shift_y + radius * k + math.sin(math.radians(angle + 90)) * radius * k * 0.7))

    points_3 = ((shift_x + radius * k + math.cos(math.radians(angle)) * radius * k * 0.4,
                 shift_y + radius * k + math.sin(math.radians(angle)) * radius * k * 0.4),
                (shift_x + radius * k + math.cos(math.radians(angle - 110)) * radius * k * 0.7,
                 shift_y + radius * k + math.sin(math.radians(angle - 110)) * radius * k * 0.7),
                (shift_x + radius * k + math.cos(math.radians(angle + 180)) * radius * k * 0.1,
                 shift_y + radius * k + math.sin(math.radians(angle + 180)) * radius * k * 0.1),
                (shift_x + radius * k + math.cos(math.radians(angle + 110)) * radius * k * 0.7,
                 shift_y + radius * k + math.sin(math.radians(angle + 110)) * radius * k * 0.7))

    points_4 = ((shift_x + radius * k, shift_y + radius * k),
                (shift_x + radius * k + math.cos(math.radians(angle - 130)) * radius * k * 0.8,
                 shift_y + radius * k + math.sin(math.radians(angle - 130)) * radius * k * 0.8),
                (shift_x + radius * k + math.cos(math.radians(angle + 180)) * radius * k * 0.4,
                 shift_y + radius * k + math.sin(math.radians(angle + 180)) * radius * k * 0.4),
                (shift_x + radius * k + math.cos(math.radians(angle + 130)) * radius * k * 0.8,
                 shift_y + radius * k + math.sin(math.radians(angle + 130)) * radius * k * 0.8))

    pygame.draw.polygon(image, color_2, points_4)
    pygame.draw.polygon(image, (0, 0, 0), points_4, 2)

    pygame.draw.polygon(image, color_1, points_3)
    pygame.draw.polygon(image, (0, 0, 0), points_3, 2)

    pygame.draw.polygon(image, color_2, points_2)
    pygame.draw.polygon(image, (0, 0, 0), points_2, 2)

    pygame.draw.polygon(image, color_1, points_1)
    pygame.draw.polygon(image, (0, 0, 0), points_1, 2)


def draw_sprite4(image, radius, angle, color_1, color_2, k=1.5, shift_x=0, shift_y=0):
    points_1 = ((shift_x + radius * k + math.cos(math.radians(angle + 30)) * radius * k,
                 shift_y + radius * k + math.sin(math.radians(angle + 30)) * radius * k),
                (shift_x + radius * k + math.cos(math.radians(angle - 165)) * radius * k,
                 shift_y + radius * k + math.sin(math.radians(angle - 165)) * radius * k),
                (shift_x + radius * k + math.cos(math.radians(angle - 30)) * radius * k,
                 shift_y + radius * k + math.sin(math.radians(angle - 30)) * radius * k),
                (shift_x + radius * k + math.cos(math.radians(angle + 165)) * radius * k,
                 shift_y + radius * k + math.sin(math.radians(angle + 165)) * radius * k))

    points_2 = ((shift_x + radius * k + math.cos(math.radians(angle)) * radius * k,
                 shift_y + radius * k + math.sin(math.radians(angle)) * radius * k),
                (shift_x + radius * k + math.cos(math.radians(angle - 160)) * radius * k * 0.6,
                 shift_y + radius * k + math.sin(math.radians(angle - 160)) * radius * k * 0.6),
                (shift_x + radius * k + math.cos(math.radians(angle + 160)) * radius * k * 0.6,
                 shift_y + radius * k + math.sin(math.radians(angle + 160)) * radius * k * 0.6))

    pygame.draw.polygon(image, color_1, points_2)
    pygame.draw.polygon(image, (0, 0, 0), points_2, 2)

    pygame.draw.polygon(image, color_2, points_1)
    pygame.draw.polygon(image, (0, 0, 0), points_1, 2)


# Инициализация шрифтов
def init_fonts():
    global FPS, SELECT_FONT, COLOR_1_FONT, COLOR_2_FONT
    FPS = pygame.font.Font(None, 18).render(f'FPS: {int(CLOCK.get_fps())}', 1, (0, 0, 0))
    SELECT_FONT = pygame.font.Font(None, 40).render('*SELECTED*', 1, (20, 180, 0))
    COLOR_1_FONT = pygame.font.Font(None, 40).render('COLOR 1:', 1, (20, 180, 0))
    COLOR_2_FONT = pygame.font.Font(None, 40).render('COLOR 2:', 1, (20, 180, 0))


def init_sounds():
    global BUTTON_SOUND, FINISH_SOUND, LOSE_SOUND, COUNTDOWN_SOUND, THRUST_SOUND
    BUTTON_SOUND = pygame.mixer.Sound('sounds/button.wav')
    BUTTON_SOUND.set_volume(0.3)
    FINISH_SOUND = pygame.mixer.Sound('sounds/finish.wav')
    FINISH_SOUND.set_volume(0.5)
    LOSE_SOUND = pygame.mixer.Sound('sounds/lose.flac')
    LOSE_SOUND.set_volume(0.3)
    COUNTDOWN_SOUND = pygame.mixer.Sound('sounds/countdown.wav')
    COUNTDOWN_SOUND.set_volume(0.4)
    THRUST_SOUND = pygame.mixer.Sound('sounds/thrust.wav')
    THRUST_SOUND.set_volume(0.1)


# Характеристики разных машин
CARS = [draw_sprite1, draw_sprite2, draw_sprite3, draw_sprite4]
# Preset: (f_acc, b_acc, rot_speed, speed, particles_per, particles_par, sprite_index, health)
# Particles: [gradient:gradient_k:increase:max_lifetime:max_size:spreading:speed_k]
CAR_PRESETS = {'beginner': (270, -100, 170, 540, 80, '(255, 162, 0), (0, 0, 0):2:30:500:None:90:1', 1, 1500),
               'medium': (320, -100, 225, 750, 70, '(13, 150, 0), (0, 0, 0):1:30:1000:None:180:0.5', 2, 2500),
               'advanced': (380, -100, 330, 850, 200, '(0, 245, 255), (255, 255, 255):1:30:100:None:100:5', 3, 2000),
               'pro': (500, -100, 380, 1100, 100, '(255, 255, 255), (0, 0, 0):1.5:30:900:None:30:5', 0, 1800)}

if 'data.txt' not in os.listdir():
    f = open('data.txt', 'w', encoding='utf-8')
    data = '\n'.join(["'beginner'", '(255, 0, 0)', '(255, 255, 0)', '0', '(True, False, False, False)', '{}'])
    f.write(data)
    f.close()
load_data()


def angleTo(point2, point1):
    radius = math.hypot(point1[0] - point2[0], point1[1] - point2[1])
    if radius == 0:
        return 0
    angle = math.degrees(math.acos((point2[0] - point1[0]) / radius))
    if point2[1] < point1[1]:
        angle = 360 - angle
    angle = (angle - 90) % 360
    return angle


# Камера
class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy
        obj.float_x += self.dx
        obj.float_y += self.dy

    def apply_border(self, bor):
        bor.rect.x += self.dx
        bor.rect.y += self.dy
        bor.pos1 = (bor.pos1[0] + self.dx, bor.pos1[1] + self.dy)
        bor.pos2 = (bor.pos2[0] + self.dx, bor.pos2[1] + self.dy)

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2) - int(target.vx / target.max_speed * 0.4 * width)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2) + int(target.vy / target.max_speed * 0.4 * height)


# Стенки
class Border(pygame.sprite.Sprite):
    def __init__(self, pos1, pos2, color=None):
        super().__init__(all_sprites)
        self.add(borders)
        self.thickness = 1
        self.pos1 = x1, y1 = pos1
        self.pos2 = x2, y2 = pos2
        if x2 < x1:
            x1, x2 = x2, x1
        if y2 < y1:
            y1, y2 = y2, y1
        self.image = pygame.Surface((x2 - x1 + self.thickness, y2 - y1 + self.thickness), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x1, y1, x2 - x1 + self.thickness, y2 - y1 + self.thickness)
        self.color = color
        if color:
            pygame.draw.line(self.image, color,
                             (pos1[0] - x1, pos1[1] - y1), (x2 - pos1[0], y2 - pos1[1]), self.thickness)


# Чекпоинты
class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, pos1, pos2, visible=False, finish=False):
        super().__init__(all_sprites)
        self.finish = finish
        self.pos1 = x1, y1 = pos1
        self.pos2 = x2, y2 = pos2
        if x2 < x1:
            x1, x2 = x2, x1
        if y2 < y1:
            y1, y2 = y2, y1
        self.image = pygame.Surface((x2 - x1 + 1, y2 - y1 + 1), pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(x1, y1, x2 - x1 + 1, y2 - y1 + 1)
        if finish:
            pygame.draw.line(self.image, (255, 0, 0),
                             (pos1[0] - x1, pos1[1] - y1), (x2 - pos1[0], y2 - pos1[1]), 1)
        elif visible:
            pygame.draw.line(self.image, (0, 200, 0),
                             (pos1[0] - x1, pos1[1] - y1), (x2 - pos1[0], y2 - pos1[1]), 1)


# Частицы
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


# Игрок
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, colors, preset, checkpoints, laps, collider=False):
        super().__init__(all_sprites)
        self.radius = 20
        self.collider = collider
        self.k = 1.4
        self.image = pygame.Surface((2 * self.radius * self.k, 2 * self.radius * self.k), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.particle_point = (0, 0)

        self.float_pos = self.float_x, self.float_y = x, y
        self.vx = self.vy = 0
        self.speed = 0
        self.accelerate = 0
        self.rot_speed = 0
        self.dir = 0
        self.color1, self.color2 = colors

        self.particle_spawner = 0
        self.spawntime = pygame.time.get_ticks()

        self.applyPreset(preset)
        self.spreading = self.partciles_par[5]
        self.speed_k = self.partciles_par[6]
        self.friction = 50

        self.setDir(0)
        self.laps = laps + 1
        self.max_laps = laps
        self.checkpoints = checkpoints
        self.next_checkpoint = checkpoints[0]
        self.renderFonts()

    def renderFonts(self):
        self.health_mes = pygame.font.Font(None, 32).render('Health:', 1, (0, 0, 0))

        cur_lap = max(0, self.max_laps - self.laps)
        mes = 'Laps: ' + '/'.join([str(cur_lap), str(self.max_laps)])
        self.laps_mes = pygame.font.Font(None, 36).render(mes, 1, (0, 0, 0))

        time = pygame.time.get_ticks() - self.spawntime
        mins = time // 60000
        secs = (time - mins * 60000) // 1000
        mes = 'Time: ' + str(mins).rjust(2, '0') + ':' + str(secs).rjust(2, '0')
        self.time_mes = pygame.font.Font(None, 36).render(mes, 1, (0, 0, 0))

    def drawUI(self):
        screen.blit(self.health_mes, (5, height - self.health_mes.get_height() - 30))
        if self.health > 0:
            k = self.health / self.max_health
            color = (255 * (1 - k), 255 * k, 0)
            pygame.draw.rect(screen, color, (5, height - 25, int(200 * k), 20))
        pygame.draw.rect(screen, (0, 0, 0), (5, height - 25, 200, 20), 2)

        screen.blit(self.laps_mes, (width - self.laps_mes.get_width() - 10, 10))

        screen.blit(self.time_mes, (width - self.time_mes.get_width() - 10, 40))

    def death(self):
        THRUST_SOUND.stop()
        load_death_screen()

    def finish(self, time):
        THRUST_SOUND.stop()
        load_win_screen(time)

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
        self.draw(self.image, self.radius, angle, self.color1, self.color2, k=self.k)

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
            THRUST_SOUND.play()
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
            THRUST_SOUND.stop()
            if self.speed < 3:
                self.speed = self.vx = self.vy = 0

        point1 = self.rect.x + self.radius * self.k, self.rect.y + self.radius * self.k
        for border in borders:
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
                    if self.health:
                        impact = new_vx + math.fabs(new_vy - final_vy)
                        if impact >= 2:
                            self.health -= impact
                            if self.health <= 0:
                                self.death()

        if self.borderDist(point1, self.next_checkpoint)[0] <= self.radius:
            if self.next_checkpoint == self.checkpoints[-1]:
                self.next_checkpoint = self.checkpoints[0]
            else:
                if self.next_checkpoint == self.checkpoints[0]:
                    self.laps -= 1
                    if self.laps == 0:
                        self.finish(pygame.time.get_ticks() - self.spawntime)
                self.next_checkpoint = self.checkpoints[self.checkpoints.index(self.next_checkpoint) + 1]

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


# Кнопка меню
class Button:
    def __init__(self, rect, text, font, command, pars=None, color=(20, 180, 0), collider=False):
        buttons.append(self)
        self.rect = rect
        self.command = command
        self.pars = pars
        self.n_color = color
        self.f_color = int(color[0] * 0.7), int(color[1] * 0.7), int(color[2] * 0.7)
        self.normal_text = font.render(text, 1, color)
        self.focused_text = font.render(text, 1, self.f_color)
        self.text = self.normal_text
        self.color = color
        self.collider = collider

    def draw(self):
        screen.blit(self.text, (self.rect.x, self.rect.y))
        if self.collider:
            pygame.draw.rect(screen, self.color, self.rect, 5)


# Показ фпс
def show_fps():
    screen.blit(FPS, (width - FPS.get_width() - 5, height - FPS.get_height() - 10))


# Открыване уровня
def start_level(level):
    global buttons, all_sprites, borders, camera, player, menu, countdown, countdown_mes, PREV_LEVEL, LEVEL_TIME
    pygame.mouse.set_visible(False)
    PREV_LEVEL = level
    buttons = []
    all_sprites = pygame.sprite.Group()
    borders = pygame.sprite.Group()
    camera = Camera()
    player, LEVEL_TIME = load_level(level)
    menu = False
    COUNTDOWN_SOUND.play()
    countdown = pygame.time.get_ticks()
    countdown_mes = pygame.font.Font(None, 240).render('3', 1, (0, 0, 0))

    camera.update(player)
    for sprite in all_sprites:
        tip = type(sprite)
        if tip == Border or tip == Checkpoint:
            camera.apply_border(sprite)
        else:
            camera.apply(sprite)


# Закгрузка меню
def load_menu():
    global menu, shop, level, countdown, buttons, player
    pygame.mouse.set_visible(True)
    menu = True
    shop = False
    level = False
    countdown = None
    buttons = []
    Button(pygame.Rect(80, 250, 180, 90), 'Play', pygame.font.Font(None, 120), load_selector)
    Button(pygame.Rect(80, 350, 210, 90), 'Shop', pygame.font.Font(None, 120), load_shop)
    Button(pygame.Rect(80, 450, 170, 70), 'Exit', pygame.font.Font(None, 120), terminate)


# Ъкран проигрыша
def load_death_screen():
    global buttons
    LOSE_SOUND.play()
    load_menu()
    buttons = []
    Button(pygame.Rect(50, 150, -180, 90), 'You died', pygame.font.Font(None, 100), nothing)
    Button(pygame.Rect(100, 300, 180, 30), 'Main menu', pygame.font.Font(None, 50), load_menu)
    Button(pygame.Rect(100, 350, 150, 30), 'Try again', pygame.font.Font(None, 50), start_level, pars=PREV_LEVEL)


# Экран финиша
def load_win_screen(time):
    global buttons, BALANCE, BALANCE_MES
    FINISH_SOUND.play()
    s_time = time // 100 / 10
    if PREV_LEVEL not in RECORDS:
        if s_time > LEVEL_TIME:
            money = 0
        else:
            money = int((LEVEL_TIME - s_time) / LEVEL_TIME * LEVEL_MONEY)
        RECORDS[PREV_LEVEL] = s_time
    elif RECORDS[PREV_LEVEL] > s_time:
        money = int((RECORDS[PREV_LEVEL] - s_time) / RECORDS[PREV_LEVEL] * LEVEL_MONEY)
        RECORDS[PREV_LEVEL] = s_time
    else:
        money = 0
    BALANCE += money
    BALANCE_MES = pygame.font.Font(None, 120).render('$' + str(BALANCE), 1, (20, 180, 0))
    save_data()
    load_menu()
    buttons = []
    Button(pygame.Rect(50, 100, -180, 90), 'You finished!', pygame.font.Font(None, 100), nothing)
    Button(pygame.Rect(50, 200, -180, 90), 'You gained ' + str(money) + '$', pygame.font.Font(None, 100), nothing)
    Button(pygame.Rect(100, 300, 180, 30), 'Main menu', pygame.font.Font(None, 50), load_menu)
    Button(pygame.Rect(100, 350, 100, 30), 'Shop', pygame.font.Font(None, 50), load_shop)


# Меню выбора уровня
def load_selector():
    global buttons
    buttons = []
    for i in range(12):
        lvl = 'lvl_' + str(i + 1) + '.txt'
        s = 'Level ' + str(i + 1)
        if lvl in RECORDS.keys():
            s += ' - ' + str(RECORDS[lvl]) + 's'
        Button(pygame.Rect(80, 40 + i * 45, 330, 40), s, pygame.font.Font(None, 60), start_level, pars=lvl)
    Button(pygame.Rect(80, 650, 195, 70), 'Back', pygame.font.Font(None, 120), load_menu)


# Магазин
def load_shop():
    global shop, buttons
    shop = True
    buttons = []
    Button(pygame.Rect(80, 650, 195, 70), 'Back', pygame.font.Font(None, 120), load_menu)
    Button(pygame.Rect(70, 140, 180, 280), 'BEGINNER'.rjust(10, ' '),
           pygame.font.Font(None, 40), select_car, pars='beginner')
    if UNLOCKED_CARS[1]:
        Button(pygame.Rect(300, 140, 180, 280), 'MEDIUM'.rjust(10, ' '),
               pygame.font.Font(None, 40), select_car, pars='medium')
    else:
        Button(pygame.Rect(300, 140, 180, 280), ('$' + str(MEDIUM_PRICE)).rjust(11, ' '),
               pygame.font.Font(None, 40), buy_car, pars=1)

    if UNLOCKED_CARS[2]:
        Button(pygame.Rect(530, 140, 180, 280), 'ADVANCED'.rjust(10, ' '),
               pygame.font.Font(None, 40), select_car, pars='advanced')
    else:
        Button(pygame.Rect(530, 140, 180, 280), ('$' + str(ADVANCED_PRICE)).rjust(11, ' '),
               pygame.font.Font(None, 40), buy_car, pars=2)

    if UNLOCKED_CARS[3]:
        Button(pygame.Rect(760, 140, 180, 280), 'PRO'.rjust(10, ' '),
               pygame.font.Font(None, 40), select_car, pars='pro')
    else:
        Button(pygame.Rect(760, 140, 180, 280), ('$' + str(PRO_PRICE)).rjust(11, ' '),
               pygame.font.Font(None, 40), buy_car, pars=3)

    colors = []
    for r in range(2):
        for g in range(2):
            for b in range(2):
                colors.append((r * 255, g * 255, b * 255))
    for i, color in enumerate(colors):
        Button(pygame.Rect(500 + i * 60, 550, 50, 50), '', pygame.font.Font(None, 40),
               change_color1, collider=True, pars=color)
        Button(pygame.Rect(500 + i * 60, 650, 50, 50), '', pygame.font.Font(None, 40),
               change_color2, collider=True, pars=color)


# Функция смены машины
def select_car(key):
    global CUR_CAR
    CUR_CAR = CAR_PRESETS[key]
    save_data()


# Функция покупки машины
def buy_car(index):
    global BALANCE, BALANCE_MES, UNLOCKED_CARS
    if index == 1:
        price = MEDIUM_PRICE
    elif index == 2:
        price = ADVANCED_PRICE
    else:
        price = PRO_PRICE
    if price <= BALANCE:
        BALANCE -= price
        BALANCE_MES = pygame.font.Font(None, 120).render('$' + str(BALANCE), 1, (20, 180, 0))
        l = list(UNLOCKED_CARS)
        l[index] = True
        UNLOCKED_CARS = tuple(l)
        save_data()
        load_shop()


# Функции смены цветов
def change_color1(color):
    global COLOR_1
    COLOR_1 = color
    save_data()


def change_color2(color):
    global COLOR_2
    COLOR_2 = color
    save_data()


CLOCK = pygame.time.Clock()

RENDERFONTS = 30
pygame.time.set_timer(RENDERFONTS, 200)
init_fonts()
init_sounds()

load_menu()

while True:
    EVENTS = pygame.event.get()
    TIME = CLOCK.tick() / 1000
    for event in EVENTS:
        if event.type == pygame.QUIT:
            terminate()

        if event.type == RENDERFONTS:
            FPS = pygame.font.Font(None, 18).render(f'FPS: {int(CLOCK.get_fps())}', 1, (0, 0, 0))
            if level:
                player.renderFonts()
            if countdown:
                mes = str(3 - int(pygame.time.get_ticks() - countdown) // 1000)
                countdown_mes = pygame.font.Font(None, 240).render(mes, 1, (0, 0, 0))

    if level:
        screen.fill((200, 200, 200))
        for event in EVENTS:
            if event.type == pygame.KEYDOWN:
                if event.key == 273:
                    player.accelerate = player.forward_accelerate
                if event.key == 274:
                    player.accelerate = player.backward_accelerate
                if event.key == 275:
                    player.rot_speed = player.max_rot_speed
                if event.key == 276:
                    player.rot_speed = -player.max_rot_speed
                if event.key == 27:
                    THRUST_SOUND.stop()
                    load_menu()

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
        player.drawUI()
        all_sprites.update()
        camera.update(player)
        for sprite in all_sprites:
            tip = type(sprite)
            if tip == Border or tip == Checkpoint:
                camera.apply_border(sprite)
            else:
                camera.apply(sprite)

    elif countdown:
        screen.fill((200, 200, 200))
        all_sprites.draw(screen)
        player.drawUI()
        screen.blit(countdown_mes, (width // 2 - countdown_mes.get_width() // 2,
                                    height // 2 - countdown_mes.get_height() // 2 - 180))
        if pygame.time.get_ticks() - countdown >= 3000:
            level = True
            countdown = None
            player.spawntime = pygame.time.get_ticks()

    elif menu:
        screen.fill((200, 200, 200))
        if shop:
            if UNLOCKED_CARS[0]:
                draw_sprite2(screen, 80, 270, COLOR_1, COLOR_2, shift_x=40, shift_y=180)
                if CUR_CAR[-2] == 1:
                    pygame.draw.rect(screen, (20, 180, 0), (70, 170, 180, 250), 3)
                    screen.blit(SELECT_FONT, (75, 430))
            else:
                draw_sprite2(screen, 80, 270, (0, 0, 0), (0, 0, 0), shift_x=40, shift_y=180)

            if UNLOCKED_CARS[1]:
                draw_sprite3(screen, 80, 270, COLOR_1, COLOR_2, shift_x=270, shift_y=180)
                if CUR_CAR[-2] == 2:
                    pygame.draw.rect(screen, (20, 180, 0), (300, 170, 180, 250), 3)
                    screen.blit(SELECT_FONT, (305, 430))
            else:
                draw_sprite3(screen, 80, 270, (0, 0, 0), (0, 0, 0), shift_x=270, shift_y=180)

            if UNLOCKED_CARS[2]:
                draw_sprite4(screen, 80, 270, COLOR_1, COLOR_2, shift_x=500, shift_y=180)
                if CUR_CAR[-2] == 3:
                    pygame.draw.rect(screen, (20, 180, 0), (530, 170, 180, 250), 3)
                    screen.blit(SELECT_FONT, (535, 430))
            else:
                draw_sprite4(screen, 80, 270, (0, 0, 0), (0, 0, 0), shift_x=500, shift_y=180)

            if UNLOCKED_CARS[3]:
                draw_sprite1(screen, 80, 270, COLOR_1, COLOR_2, shift_x=730, shift_y=180)
                if CUR_CAR[-2] == 0:
                    pygame.draw.rect(screen, (20, 180, 0), (760, 170, 180, 250), 3)
                    screen.blit(SELECT_FONT, (765, 430))
            else:
                draw_sprite1(screen, 80, 270, (0, 0, 0), (0, 0, 0), shift_x=730, shift_y=180)
            screen.blit(BALANCE_MES, (80, 30))

            colors = []
            for r in range(2):
                for g in range(2):
                    for b in range(2):
                        colors.append((r * 255, g * 255, b * 255))
            for i, color in enumerate(colors):
                screen.blit(COLOR_1_FONT, (350, 560))
                screen.blit(COLOR_2_FONT, (350, 660))
                pygame.draw.rect(screen, color, (500 + i * 60, 550, 50, 50))
                pygame.draw.rect(screen, color, (500 + i * 60, 650, 50, 50))
        else:
            CARS[CUR_CAR[-2]](screen, 150, 270, COLOR_1, COLOR_2, shift_x=550, shift_y=180)
        for btn in buttons:
            btn.draw()
        for event in EVENTS:
            if event.type == pygame.MOUSEMOTION:
                for btn in buttons:
                    if btn.rect.collidepoint(event.pos):
                        btn.text = btn.focused_text
                        btn.color = btn.f_color
                    else:
                        btn.text = btn.normal_text
                        btn.color = btn.n_color
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in buttons:
                    if btn.rect.collidepoint(event.pos):
                        BUTTON_SOUND.play()
                        if btn.pars:
                            btn.command(btn.pars)
                        else:
                            btn.command()

    show_fps()
    pygame.display.flip()

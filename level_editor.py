import pygame
import math
import os


def undo(borders):
    if len(borders) > 0:
        borders = borders[:-1]
    return borders


def save(player, borders):
    b_data = []
    c_data = []
    k = input('Enter the k value: ')
    laps = input('Enter laps amount: ')
    time = input('Enter level time: ')
    for el in borders:
        if type(el) == tuple:
            if len(el) == 2:
                b_data.append(((el[0][0] - player[0], el[0][1] - player[1]),
                               (el[1][0] - player[0], el[1][1] - player[1])))
            else:
                c_data.append(((el[0][0][0] - player[0], el[0][0][1] - player[1]),
                               (el[0][1][0] - player[0], el[0][1][1] - player[1])))
        elif type(el) == list:
            for border in el:
                b_data.append(((border[0][0] - player[0], border[0][1] - player[1]),
                               (border[1][0] - player[0], border[1][1] - player[1])))
    data = '\n'.join([str(b_data), str(c_data), laps, k, time])
    levels = os.listdir('levels')
    name = 'lvl_1.txt'
    i = 1
    while name in levels:
        i += 1
        name = f'lvl_{i}.txt'
    f = open('levels/' + name, 'w', encoding='utf-8')
    f.write(data)
    f.close()


pygame.init()
size = width, height = (1024, 768)
screen = pygame.display.set_mode(size)

running = True
alt = shift = ctrl = False
player = (0, 0)
linear_drag = drag = chk_drag = None
borders = []
checkpoints = []

while running:
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if alt:
                drag = [(event.pos, event.pos)]
            elif shift:
                linear_drag = (event.pos, event.pos)
            elif ctrl:
                chk_drag = (event.pos, event.pos)
            else:
                player = event.pos

        if event.type == pygame.MOUSEMOTION:
            if linear_drag:
                linear_drag = (linear_drag[0], event.pos)
            elif chk_drag:
                chk_drag = (chk_drag[0], event.pos)
            elif drag:
                drag[-1] = (drag[-1][0], event.pos)
                if math.hypot(drag[-1][0][0] - event.pos[0], drag[-1][0][1] - event.pos[1]) >= 20:
                    drag.append((event.pos, event.pos))

        if event.type == pygame.MOUSEBUTTONUP:
            if linear_drag:
                if linear_drag[0] != linear_drag[1]:
                    borders.append(linear_drag)
                linear_drag = None
            elif chk_drag:
                if chk_drag[0] != chk_drag[1]:
                    borders.append((chk_drag,))
                chk_drag = None
            elif drag:
                if drag[-1][0] == drag[-1][1]:
                    drag = drag[:-1]
                if len(drag) > 0:
                    borders.append(drag)
                drag = None

        if event.type == pygame.KEYDOWN:
            if event.key == 308:
                alt = True
            if event.key == 304:
                shift = True
            if event.key == 306:
                ctrl = True
            if event.key == 122 and event.mod == 64:
                borders = undo(borders)
            if event.key == 115 and event.mod == 64:
                save(player, borders)

        if event.type == pygame.KEYUP:
            if event.key == 308:
                alt = False
            if event.key == 304:
                shift = False
            if event.key == 306:
                ctrl = False

    # draw player
    pygame.draw.circle(screen, (255, 0, 0), player, 4)

    # draw drags
    if linear_drag:
        if linear_drag[0] != linear_drag[1]:
            pygame.draw.line(screen, (0, 0, 0), (linear_drag[0]), (linear_drag[1]))
    elif chk_drag:
        if chk_drag[0] != chk_drag[1]:
            pygame.draw.line(screen, (0, 200, 0), (chk_drag[0]), (chk_drag[1]))
    elif drag:
        for line in drag:
            if line[0] != line[1]:
                pygame.draw.line(screen, (0, 0, 0), line[0], line[1])

    # draw borders
    for el in borders:
        if type(el) == tuple:
            if len(el) == 2:
                pygame.draw.line(screen, (0, 0, 0), (el[0]), (el[1]))
            else:
                pygame.draw.line(screen, (0, 200, 0), (el[0][0]), (el[0][1]))
        elif type(el) == list:
            for border in el:
                pygame.draw.line(screen, (0, 0, 0), (border[0]), (border[1]))

    pygame.display.flip()

pygame.quit()

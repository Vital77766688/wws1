import pygame
import random
import math

SCREEN_DIM = (800, 600)

class Vec2d:

    def __init__(self, x):
        self.x = x

    @staticmethod
    def int_pair(x, y) -> tuple:
        return x, y

    def __add__(self, other):
        return self.x[0] + other.x[0], self.x[1] + other.x[1]

    def __sub__(self, other):
        return self.x[0] - other.x[0], self.x[1] - other.x[1]

    def __mul__(self, other):
        if not isinstance(other, int):
            return self.x[0] * other.x, self.x[1] * other.x
        return self.x[0] * other, self.x[1] * other

    def __len__(self):
        return math.sqrt(self.x[0] * self.x[0] + self.x[1] * self.x[1])



class Polyline:

    # "Отрисовка" точек
    def draw_points(self, points, style="points", width=3, color=(255, 255, 255)):
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color, (int(points[p_n][0]), int(points[p_n][1])),
                                 (int(points[p_n + 1][0]), int(points[p_n + 1][1])), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color,
                                   (int(p[0]), int(p[1])), width)

    # Сглаживание ломаной
    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return add(mul(points[deg], alpha), mul(get_point(points, alpha, deg - 1), 1 - alpha))

    def get_points(self, base_points, count):
        alpha = 1 / count
        res = []
        for i in range(count):
            res.append(self.get_point(base_points, i * alpha))
        return res

    def get_knot(self, points, count):
        if len(points) < 3:
            return []
        res = []
        for i in range(-2, len(points) - 2):
            ptn = []
            ptn.append(mul(add(points[i], points[i + 1]), 0.5))
            ptn.append(points[i + 1])
            ptn.append(mul(add(points[i + 1], points[i + 2]), 0.5))

            res.extend(self.get_points(ptn, count))
        return res

    # Персчитывание координат опорных точек
    def set_points(self, points, speeds):
        for p in range(len(points)):
            points[p] = add(points[p], speeds[p])
            if points[p][0] > SCREEN_DIM[0] or points[p][0] < 0:
                speeds[p] = (- speeds[p][0], speeds[p][1])
            if points[p][1] > SCREEN_DIM[1] or points[p][1] < 0:
                speeds[p] = (speeds[p][0], -speeds[p][1])


class Knot(Polyline):
    pass


# Основная программа
if __name__ == "__main__":
    pygame.init()
    gameDisplay = pygame.display.set_mode(SCREEN_DIM)
    pygame.display.set_caption("MyScreenSaver")

    steps = 35
    working = True
    points = []
    speeds = []
    show_help = False
    pause = True

    hue = 0
    color = pygame.Color(0)

    while working:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                working = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    working = False
                if event.key == pygame.K_r:
                    points = []
                    speeds = []
                if event.key == pygame.K_p:
                    pause = not pause
                if event.key == pygame.K_KP_PLUS:
                    steps += 1
                if event.key == pygame.K_F1:
                    show_help = not show_help
                if event.key == pygame.K_KP_MINUS:
                    steps -= 1 if steps > 1 else 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                points.append(event.pos)
                speeds.append((random.random() * 2, random.random() * 2))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        #draw_points(points)
        #draw_points(get_knot(points, steps), "line", 3, color)
        #if not pause:
        #    set_points(points, speeds)
        #if show_help:
        #    draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
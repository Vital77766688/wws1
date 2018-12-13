import pygame
import random
import math

SCREEN_DIM = (800, 600)

class Vec2d:

    def __init__(self, x):
        self.x = x
        self.x1 = x[0]
        self.x2 = x[1]

    def int_pair(self) -> tuple:
        return int(self.x1), int(self.x2)

    def __add__(self, other):
        return Vec2d((self.x1 + other.x1, self.x2 + other.x2))

    def __sub__(self, other):
        return Vec2d((self.x1 - other.x1, self.x2 - other.x2))

    def __mul__(self, other):
        if isinstance(other, tuple):
            return Vec2d((self.x1 * self.other.x, self.x2 * other.x))
        return Vec2d((self.x1 * other, self.x2 * other))

    def __len__(self):
        return math.sqrt(self.x1 * self.x1 + self.x2 * self.x2)



class Polyline:

    # "Отрисовка" точек
    def draw_points(self, points, style="points", width=3, color=(255, 255, 255)):
        if style == "line":
            for p_n in range(-1, len(points) - 1):
                pygame.draw.line(gameDisplay, color, points[p_n].int_pair(), points[p_n + 1].int_pair(), width)

        elif style == "points":
            for p in points:
                pygame.draw.circle(gameDisplay, color, p.int_pair(), width)

    # Сглаживание ломаной
    def get_point(self, points, alpha, deg=None):
        if deg is None:
            deg = len(points) - 1
        if deg == 0:
            return points[0]
        return points[deg] * alpha + self.get_point(points, alpha, deg - 1) * (1 - alpha)

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
            #ptn.append(mul(add(points[i], points[i + 1]), 0.5))
            #ptn.append(points[i + 1])
            #ptn.append(mul(add(points[i + 1], points[i + 2]), 0.5))
            ptn.append((points[i] + points[i + 1]) * 0.5)
            ptn.append(points[i + 1])
            ptn.append((points[i + 1] + points[i + 2]) * 0.5)

            res.extend(self.get_points(ptn, count))
        return res

    # Персчитывание координат опорных точек
    def set_points(self, points, speeds):
        for p in range(len(points)):
            points[p] = points[p] + speeds[p]
            if points[p].x1 > SCREEN_DIM[0] or points[p].x1 < 0:
                speeds[p] = Vec2d((- speeds[p].x1, speeds[p].x2))
            if points[p].x2 > SCREEN_DIM[1] or points[p].x2 < 0:
                speeds[p] = Vec2d((speeds[p].x1, -speeds[p].x2))


class Knot(Polyline):

    def draw_line(self, points, width=3, color=(255,255,255)):
        pass

    def draw_circle(self):
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
                points.append(Vec2d(event.pos))
                speeds.append(Vec2d((random.random() * 2, random.random() * 2)))

        gameDisplay.fill((0, 0, 0))
        hue = (hue + 1) % 360
        color.hsla = (hue, 100, 50, 100)
        dots = Polyline()
        dots.draw_points(points)
        dots.draw_points(dots.get_knot(points, steps), "line", 3, color)
        if not pause:
            dots.set_points(points, speeds)
        #if show_help:
        #    draw_help()

        pygame.display.flip()

    pygame.display.quit()
    pygame.quit()
    exit(0)
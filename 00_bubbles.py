# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей


point = sd.get_point(600, 300)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius, width=2)


# Написать функцию рисования пузырька, принимающую 2 (или более) параметра: точка рисования и шаг


def buble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)


point = sd.get_point(300, 300)
buble(point=point, step=10)


# Нарисовать 10 пузырьков в ряд


def buble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)

for x in range(100, 1001, 100):
    point = sd.get_point(x, 100)
    buble(point=point, step=5)


# Нарисовать три ряда по 10 пузырьков


def buble(point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)
for x in range (100, 1001, 100):
    for y in range (200, 401, 100):
        point = sd.get_point(x, y)
        buble(point=point, step=5)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами


def buble (point, step):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2)
for x in range(100):
    point = sd.random_point()
    buble(point=point, step=20)


sd.pause()



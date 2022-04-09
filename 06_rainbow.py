# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd


rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# x1 = 50
# x2 = 350
#
# for _ in range(len(rainbow_colors)):
#     x1 += 4
#     x2 += 4
#     sd.line(sd.get_point(x1, 50), sd.get_point(x2, 450), color=rainbow_colors[_], width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


point = sd.get_point(300, 0)
radius = 400
for _ in range(len(rainbow_colors)):
    radius += 15
    sd.circle(center_position=point, radius=radius, color=rainbow_colors[_], width=15)

sd.pause()

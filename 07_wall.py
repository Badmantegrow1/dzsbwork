# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd



# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
#размеры кирпича он же шаг отступа

for y in range(0, 600, 50):
    x = int(y / 50) % 2 * 50
    for x in range(x, 600, 100):
        sd.rectangle(sd.get_point(x, y), sd.get_point(x + 100, y + 50), width=2)

sd.pause()

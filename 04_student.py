# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
month = 1
sum_educational = 0
sum_expenses = 0

while month <= 10:
    month += 1
    sum_educational += educational_grant
    sum_expenses += expenses
    expenses += ((expenses / 100) * 3)
sum_ob = sum_expenses - sum_educational

print("Всего доходов за 10 месяцев:", sum_educational, "руб.")
print("Всего расходов за 10 месяцев:", round(sum_expenses, 2), "руб.")
print("У родителей нужно попросить:", round(sum_ob, 2), 'руб.')

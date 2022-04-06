# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом


def user():
    user_input = input("Введите, пожалуйста, номер месяца: ")
    if user_input.isalpha() or not user_input.isnumeric():
        print('Вы ввели неверное значение!')
        return
    if user_input == '':
        print('Вы ничего не указали!')
        return
    else:
        month = int(user_input)
    if month <= 0 or month >= 13:
        print("Вы ввели не корретные данные, диапазон чисел должен быть от 1-го до 12-ти!")
    elif month >= 1 or month <= 12:
        list_month = ['Январь - 31 день', 'Февраль - 28 дней', 'Март - 31 день', 'Апрель - 30 дней', 'Май - 31 день',
                      'Июнь - 30 дней', 'Июль - 31 день', 'Август - 31 день', 'Сентябрь - 30 дней', 'Октябрь - 31 день',
                      'Ноябрь - 30 дней', 'Декабрь - 31 день']
        print("Ввод корректный, вы выбрали:", list_month[month - 1])
    else:
        print("Не корректные данные!")


user()
while True:
    q = input("Продолжить? (Да|Нет):\n")
    if q.lower() == 'да':
        user()
    elif q.lower() == 'нет':
        exit()
    else:
        print("Не верный ввод")
        continue

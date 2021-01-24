""""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def convert_to_number(number_var):
    try:
        number_var = float(number_var)
    except ValueError as error_text:
        number_var = error_text
    return number_var


def check_input(user_input):
    user_input = convert_to_number(user_input)
    while user_input == '' or str(type(user_input)) == "<class 'ValueError'>":
        # print(user_input)
        user_input = convert_to_number(input("Введите действительное число: "))
    return user_input


def division_numbers(user_numerator, user_denominator):
    try:
        result = user_numerator / user_denominator
        print(f"Результатом деления {user_numerator} на {user_denominator} будет {result}")
    except ZeroDivisionError:
        print("Ошибка, деление на ноль. Вы указали значение для знаменателя ноль")


numerator = check_input(input("Введите числитель: "))
denominator = check_input(input("Введите знаменатель: "))
division_numbers(numerator, denominator)
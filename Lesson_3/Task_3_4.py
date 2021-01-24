"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
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
        user_input = convert_to_number(input("Введите требуемое число: "))
    return user_input


def number_in_power_1(number, power):
    # первый способ - через **
    result = number ** power
    return result


def number_in_power_2(number, power):
    # второй способ - рекурсия
    power = abs(power)

    def denominator(number_d, power_d):
        if power_d == 1:
            return number_d
        else:
            return number_d * denominator(number_d, power_d - 1)

    result = 1 / denominator(number, power)
    return result


def number_in_power_3(number, power):
    # третий способ - цикл
    power = abs(power)
    result = number
    for i in range(1, power):
        result *= number
    return 1 / result


user_number = abs(check_input(input("Введите действительное число: ")))
user_power_number = int(check_input(input("Введите целое число: ")))
user_power_number = user_power_number if user_power_number < 0 else user_power_number * (-1)

print(f"Способ №1. Результат возведения числа {user_number} "
      f"в степень {user_power_number} "
      f"составит: {number_in_power_1(user_number, user_power_number)}")

print(f"Способ №2. Результат возведения числа {user_number} "
      f"в степень {user_power_number} "
      f"составит: {number_in_power_2(user_number, user_power_number)}")

print(f"Способ №3. Результат возведения числа {user_number} "
      f"в степень {user_power_number} "
      f"составит: {number_in_power_3(user_number, user_power_number)}")

print(f" контролька {pow(user_number, user_power_number)}")

"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов."""


def convert_to_number(number_var):
    try:
        number_var = float(number_var)
    except ValueError as error_text:
        number_var = error_text
    return number_var


def check_input(user_input):
    user_input = convert_to_number(user_input)
    while user_input == '' or str(type(user_input)) == "<class 'ValueError'>":
        user_input = convert_to_number(input("Введите действительное число: "))
    return user_input


def my_func(number_1, number_2, number_3):
    result = list(locals().values())

    # # 1 способ
    max_1 = max(result)
    result.remove(max_1)
    max_2 = max(result)
    result =  max_1 + max_2

    # # второй способ
    # result = sum(result) - min(result)

    return result

user_input_1 = check_input(input("Введите первое число: "))
user_input_2 = check_input(input("Введите второе число: "))
user_input_3 = check_input(input("Введите третье число: "))

print(f"Сумма дыух максимальных елементов составит {my_func(user_input_1, user_input_2, user_input_3)}")

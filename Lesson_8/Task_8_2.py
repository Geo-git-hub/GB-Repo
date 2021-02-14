"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
 Проверьте его работу на данных, вводимых пользователем.
 При вводе пользователем нуля в качестве делителя программа должна корректно
 обработать эту ситуацию и не завершиться с ошибкой.
"""


class CheckError(Exception):
    def __init__(self, error_text):
        self.error_text = error_text


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


user_input_numerator = check_input(input('Введите числитель:'))
user_input_denominator = check_input(input('Введите знаменатель:'))

try:
    if user_input_denominator == 0:
        raise CheckError('Знаменатель равен нулю. На ноль делить нельзя.')

    answer = user_input_numerator / user_input_denominator

except CheckError as error_txt:
    print(error_txt)

else:
    print(f'Результатом деления {user_input_numerator} на {user_input_denominator} будет {answer}')

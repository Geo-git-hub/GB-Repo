"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
 При нажатии Enter должна выводиться сумма чисел.
 Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
 Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
 Но если вместо числа вводится специальный символ, выполнение программы завершается.
 Если специальный символ введен после нескольких чисел,
 то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

number_list = []
continue_condition = True


def convert_to_number(number_var):
    try:
        number_var = float(number_var)
    except ValueError as error_text:
        if number_var == 'q':
            number_var = False  # специальный символ для завершения программы - q
        elif str(type(error_text)) == "<class 'ValueError'>":
            return  # будет None если ввели текст - будет игнорироваться
    return number_var


while continue_condition:
    user_string = input("Ведите строку чисел, разделённых пробелом ( q - для завершения программы):")
    user_list = list(user_string.split())
    current_list = []
    for element in user_list:
        number = convert_to_number(element)
        if number is None:
            continue
        elif number is False:
            continue_condition = False
            break
        else:
            current_list.append(number)
    print(f"Сумма чисел составила: {sum(current_list)}")
    number_list.extend(current_list)

print(f"Итоговая сумма чисел составила: {sum(number_list)}")

"""Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input()."""
user_char = input("Вводите элементы массива по одному. Для заверщения введите 'пробел' ")
user_list = []
result_list = []

while not user_char == ' ':
    user_list.append(user_char)
    user_char = input("Вводите элементы массива по одному. Для заверщения введите 'пробел' ")


def revers_func(list_to_revers, count_chars):
    i = 0
    revers_list = []
    while i < count_chars:
        revers_list.append(list_to_revers[i + 1])
        revers_list.append(list_to_revers[i])
        i += 2
    return revers_list


if len(user_list) <= 1:
    print(f'Введённый массив: {user_list}')
    print(f'Итоговый массив: {user_list}')
else:
    if (len(user_list) % 2) == 0:
        result_list = revers_func(user_list, len(user_list))
    elif (len(user_list) % 2) != 0:
        result_list = revers_func(user_list, len(user_list) - 1)
        result_list.append(user_list[len(user_list) - 1])
    print(f'Введённый массив: {user_list}')
    print(f'Итоговый массив: {result_list}')

# второй способ==============================================================================================
user_list = []
result_list = []
user_char = input("Вводите элементы массива по одному. Для заверщения введите 'пробел' ")

while not user_char == ' ':
    user_list.append(user_char)
    if (len(user_list) % 2) == 0:
        result_list.insert(len(result_list) - 1, user_char)
    else:
        result_list.append(user_char)
    user_char = input("Вводите элементы массива по одному. Для заверщения введите 'пробел' ")

print(f'Введённый массив: {user_list}')
print(f'Итоговый массив: {result_list}')
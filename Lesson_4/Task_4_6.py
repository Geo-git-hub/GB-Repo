"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

start = 3


def int_in_count(start_f, stop_f=10):
    int_list = []
    for el in count(start_f):
        if el >= stop_f:
            break
        else:
            int_list.append(el)
    return int_list


int_number_list = int_in_count(start)
print(int_number_list)


# Способ 1---------------------------------------
def cycle_list(stop_f, init_list):
    answer_list = []
    cycle_count = 0
    stop_f *= len(init_list)
    for el in cycle(init_list):
        if cycle_count < stop_f:
            answer_list.append(el)
            cycle_count += 1
        else:
            break
    return answer_list


print(f'Первый способ {cycle_list(5, int_number_list)}')


# Способ 2-----------------------------------------------

def cycle_list_2(stop_f, init_list):
    answer_list = []

    for el in init_list:
        cycle_count = 0
        for i_el in cycle([el]):
            if cycle_count < stop_f:
                answer_list.append(i_el)
                cycle_count += 1
            else:
                break
    return answer_list


print(f'Второй способ {cycle_list_2(5, int_number_list)}')

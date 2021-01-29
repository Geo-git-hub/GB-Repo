"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

initial_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


# Способ №1-------------------------------------------------------
def more_than_previous(init_list):
    for index, el in enumerate(init_list[1:]):
        if el > init_list[index]:
            yield el


generator_list = more_than_previous(initial_list)
answer_list = []
for x in generator_list:
    answer_list.append(x)

print(answer_list)

# № Способ №2----------------------------------------------------------------------
q = [x for el, x in enumerate(initial_list[1:]) if x > initial_list[el]]
print(q)

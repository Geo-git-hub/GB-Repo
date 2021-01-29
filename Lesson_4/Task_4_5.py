"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce


def even_number_product(first, second):
    return first * second


print(reduce(even_number_product, [x for x in range(100, 1001) if not x % 2]))

"""
Создать (программно) текстовый файл, записать в него программно набор чисел,
 разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import random, randint, randrange

with open('user_file_5.txt', 'w+') as user_file:
    line = ''
    for num in range(1, randint(10, 20)):
        line += str(randrange(10, 101)) + ' '   # str(round(random() * 100, 2)) + ' '

    user_file.writelines(line)
    user_file.seek(0)

    content = user_file.readlines()
    content = content[0].split(' ')

    element_sum = sum(float(el) for el in content[:-1])

    print(content)
    print(round(element_sum, 2))

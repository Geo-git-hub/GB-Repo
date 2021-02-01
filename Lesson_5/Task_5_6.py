"""
Необходимо создать (не программно) текстовый файл,
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def symbol_number(line_f):  # обработка строки и получение суммы чисел
    lesson_count = 0
    for word in line_f[1:]:
        num = '0'
        for symbol_f in word:
            if symbol_f.isdigit() or symbol_f == '0':
                num += symbol_f
        lesson_count += int(num)
    return lesson_count


dict_lessons = {}

with open('user_file_6.txt', 'r') as user_file:
    content = user_file.readlines()
    for line in content:
        line_content = line.split(' ')
        sum_of_lessons = symbol_number(line_content)
        lesson = line_content[0]
        dict_lessons[lesson[:-1]] = sum_of_lessons

print(dict_lessons)

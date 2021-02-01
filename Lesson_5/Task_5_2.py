"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open('user_file_2.txt') as user_file:
    print(user_file.read())
    user_file.seek(0)

    content = [line[:-1] for line in user_file if line != '']

    print(f'\n\nВ файле {len(content)} строки\n')

    for num, el in enumerate(content, start=1):
        # words = len(el.split(' '))
        print(f'В строке {num} - {len(el.split(" "))} слов')

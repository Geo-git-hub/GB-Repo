"""
Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('user_file_1.txt', 'w+') as user_file:
    while (user_input := input(f'Введите строку (для завершения введите пустую строку): ')) != '':
        user_file.write(f'{user_input} \n')
    user_file.seek(0)
    content = user_file.read()
    print(f'\nВы ввели: \n{content}')

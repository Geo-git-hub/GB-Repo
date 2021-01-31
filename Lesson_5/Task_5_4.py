"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
dict_rus = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}

with open('user_file_4_1.txt') as user_file_1:
    with open('user_file_4_2.txt', 'w') as user_file_2:

        for line in user_file_1:
            content_1 = line.lower() if line[len(line) - 1] != '\n' else line[:-1].lower()
            content_1 = content_1.split(' ')
            content_2 = []

            for word in content_1:
                if dict_rus.get(word):
                    content_2.append(dict_rus.get(word).title())
                else:
                    content_2.append(word)

            content_2.append('\n')

            user_file_2.writelines(' '.join(content_2))

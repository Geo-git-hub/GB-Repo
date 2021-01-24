"""Пользователь вводит строку из нескольких слов, разделённых пробелами.
 Вывести каждое слово с новой строки.
 Строки необходимо пронумеровать.
 Если в слово длинное, выводить только первые 10 букв в слове."""

user_input = input("Введите строку (разделив слова пробелами): ")

while len(user_input) == 0:
    user_input = input("Введите строку (разделив слова пробелами): ")

user_list = user_input.split()
for element in user_list:
    if len(element) < 10:
        print(f"{user_list.index(element) + 1} is: {element}")
    else:
        print(f"{user_list.index(element) + 1} is: {element[0:10]}")
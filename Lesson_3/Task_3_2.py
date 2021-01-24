"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 - имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

user_name = input("Укажите имя: ")
user_surname = input("Укажите фамилию: ")
user_date = input("Укажите год рождения: ")
user_city = input("Укажите город проживания: ")
user_email = input("Укажите e-mail: ")
user_phone = input("Укажите номер телефона: ")


def user_data(name, surname, city, date, phone, email):
    # print(f" имя: {name}, фамилия: {surname}, год рождения: {date},"
    #       f" e-mail: {email}, телефон: {phone}, город проживания: {city}")

    result = locals().values()
    for element in result:
        print(f" {element} ", end='')


user_data(name=user_name, city=user_city, phone=user_phone, date=user_date, email=user_email, surname=user_surname)

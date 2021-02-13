"""
Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать
число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:

    @classmethod
    def get_data(cls, data_string):
        list_q = {'day': 0, 'month': 0, 'year': 0}

        date_list = [int(el) for el in data_string.split('-')]

        for position, el in enumerate(list_q):
            if Date.data_validation(date_list[position], el):
                list_q[el] = date_list[position]
            else:
                return f'for date {data_string}, {el} is out of range'
        return list_q

    @staticmethod
    def data_validation(number, part_of_date):
        if part_of_date == 'day' and number in range(1, 32):
            return True
        elif part_of_date == 'month' and number in range(1, 13):
            return True
        elif part_of_date == 'year' and number in range(1900, 9999):
            return True
        else:
            return False


print(Date.get_data('15-06-1900'))
print(Date.get_data('32-06-1900'))
print(Date.get_data('15-13-1900'))
print(Date.get_data('0-06-1900'))

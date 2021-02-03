"""
Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname,
position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
 содержащий элементы: оклад и премия, например,
 {"wage": wage, "bonus": bonus}.
 Создать класс Position (должность) на базе класса Worker.
 В классе Position реализовать методы получения полного
 имени сотрудника (get_full_name) и дохода с учетом премии
 (get_total_income). Проверить работу примера на реальных данных
 (создать экземпляры класса Position, передать данные,
 проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'ФИО: {self.name} {self.surname}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'Доход с учетом премии: {total_income}')


q = Position('Иван', 'Иванов', 'Manager', 5000, 500)
print(f'Имя: {q.name}')
print(f'Фамилия: {q.surname}')
print(f'Должность: {q.position}')
q.get_full_name()
q.get_total_income()

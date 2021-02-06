"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки.')

    def __str__(self):
        return f'{self.title}'


class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)

    def draw(self):
        print(f'запуск отрисовки для {self.title}')


class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)

    def draw(self):
        print(f'отрисовки для {self.title}')


class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)

    def draw(self):
        print(f'рисуем при помощи {self.title}')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

stationery = [
    pen,
    pencil,
    handle
]

for el in stationery:
    print('===================================================================')
    print(el)
    el.draw()
    print('===================================================================')

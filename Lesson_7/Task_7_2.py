"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные
 классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

    @abstractmethod
    def tissue_consumption(self, volume):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Coat(Clothes):
    def __init__(self, name, volume):
        super().__init__(name, volume)

    @property
    def tissue_consumption(self):  # для пальто (V/6.5 + 0.5)
        return round(self.volume / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Для {self.name} необходимо {self.tissue_consumption} ткани.'


class Costume(Clothes):
    def __init__(self, name, volume):
        super().__init__(name, volume)

    @property
    def tissue_consumption(self):  # для костюма (2 * H + 0.3)
        return round(2 * self.volume + 0.3, 2)

    def __str__(self):
        return f'Для {self.name} необходимо {self.tissue_consumption} ткани.'


def total_volume(total_list):
    overall_volume = 0
    for el in total_list:
        overall_volume += el.tissue_consumption

    return overall_volume


print('===============================================================================')

coat_1 = Coat('model_1', 162)
print(coat_1)

print('===============================================================================')

costume_1 = Costume('model_summer_2019', 180)
print(costume_1)

print('===============================================================================')

all_clothes = [
    coat_1,
    costume_1
]
print(f'Для всех изделии необходимо {total_volume(all_clothes)} ткани.')

print('===============================================================================')

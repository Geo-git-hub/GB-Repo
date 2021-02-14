"""
4)
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class NumberExcept(Exception):
    def __init__(self, error_text):
        self.error_text = error_text


class Warehouse:
    equipment_list = []

    @staticmethod
    def check_number(number):
        try:
            number = int(number)
            if number < 0:
                raise NumberExcept('Вы указали отрицательное число')
        except ValueError as text:
            return f'Некорректно указанны данные(введён текст): {text}'
        except NumberExcept as text:
            return f'{text}'
        else:
            return number

    @classmethod
    def get_equipment(cls, equipment):
        list_to_check = ['quantity', 'price']

        check_pass = True
        for el in list_to_check:
            if str(type(Warehouse.check_number(equipment.get(el)))) == "<class 'str'>":
                check_pass = False
                print(f'Для параметра: | {el} | в объекте {equipment} \n {Warehouse.check_number(equipment.get(el))}'
                      f'\n ввод отменён.')

        if check_pass:
            Warehouse.equipment_list.append(equipment)

    @classmethod
    def receipt(cls, receipt_list):
        for el in receipt_list:
            Warehouse.get_equipment(el.__dict__)

    @classmethod
    def equipment_info(cls, type_equipment, value):
        """Укажите наименование искомого ключа и искомое значение"""
        info = f'На складе {type_equipment} - {value}: \n'
        quantity = 0
        for el in Warehouse.equipment_list:
            if el.get(type_equipment) == value:
                info += f' {el.get("name")}, код- {el.get("code")}  {el.get("quantity")} штук; \n'
                quantity += el.get("quantity")

        info += f' всего: {quantity} штук'
        return info

    @classmethod
    def give_away(cls, code, quantity):
        """Укажите код и передоваемое количество"""
        for el in Warehouse.equipment_list:
            if el.get('code') == code:
                if el['quantity'] >= quantity:
                    el['quantity'] = el['quantity'] - quantity
                    print(f'Операция проведена успешно')
                else:
                    print(f'указанное количество больше доступного, операция отменена.')


class OfficeEquipment:
    def __init__(self, name, type_equipment, code, quantity, price):
        self.name = name
        self.type_equipment = type_equipment
        self.code = code
        self.quantity = quantity
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, name, type_equipment, code, quantity, price, paper_size, printing_technology, print_speed):
        super().__init__(name, type_equipment, code, quantity, price)
        self.paper_size = paper_size
        self.printing_technology = printing_technology
        self.print_speed = print_speed

    def __str__(self):
        return f'''{self.name, self.type_equipment, self.code, self.quantity, self.price, self.paper_size,
                    self.printing_technology, self.print_speed}'''


class Scanner(OfficeEquipment):
    def __init__(self, name, type_equipment, code, quantity, price, scanner_resolution):
        super().__init__(name, type_equipment, code, quantity, price)
        self.scanner_resolution = scanner_resolution

    def __str__(self):
        return f'{self.name, self.type_equipment, self.code, self.quantity, self.price, self.scanner_resolution}'


class Xerox(OfficeEquipment):
    def __init__(self, name, type_equipment, code, quantity, price, paper_size, printing_technology, print_speed):
        super().__init__(name, type_equipment, code, quantity, price)
        self.paper_size = paper_size
        self.printing_technology = printing_technology
        self.print_speed = print_speed

    def __str__(self):
        return f'''{self.name, self.type_equipment, self.code, self.quantity, self.price, self.paper_size,
                    self.printing_technology, self.print_speed}'''

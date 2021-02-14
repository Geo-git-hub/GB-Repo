"""
Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    def __init__(self, name, address, capacity):
        self.name = name
        self.address = address
        self.capacity = capacity


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


scanner = Scanner('CanoScan LiDE 300', 'scanner', '2995C010', 100, 5600, '2400x2400 dpi')
print(scanner)

printer = Printer('ECOSYS P3155dn', 'printer', '1102TR3NL0', 32, 38000, 'A4', 'laser', 55)
print(printer)

xerox = Xerox('Xerox B215', 'xerox', 'B215DNI', 45, 20000, 'A4', 'laser', 40)
print(xerox)
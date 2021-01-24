"""Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя."""
goods_list = []


def create_product(prod_number):
    # product_count = len(goods_list) + 1
    product_name = input(f"Укажите название для продукта № {prod_number}, для выхода введите пробел:")
    if product_name == " ":
        return
    product_price = input("Укажите цену:")
    while not product_price.isnumeric():
        product_price = input("Укажите корректную цену:")
    product_quantity = input("Укажите количество:")
    while not product_price.isnumeric():
        product_price = input("Укажите корректное количество:")
    product_units = input("Укажите единицу измерения:")
    return product_name,  int(product_price), int(product_quantity), product_units

product_insert = create_product()
print(product_insert)
# while product_insert != None:
#     dict_product

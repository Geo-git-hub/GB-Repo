"""Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно,
т.е. запрашивать все данные у пользователя."""

goods_list = []


def create_product(prod_number):

    product_name = input(f"Укажите название для продукта № {prod_number}, для выхода введите пробел:")
    if product_name == " ":
        return

    product_price = input("Укажите цену:")
    while not product_price.isnumeric() or int(product_price) < 0:
        product_price = input("Укажите корректную цену:")

    product_quantity = input("Укажите количество:")
    while not product_quantity.isnumeric() or int(product_quantity) < 0:
        product_quantity = input("Укажите корректное количество:")

    product_units = input("Укажите единицу измерения:")

    dict_product = {"название": product_name, "цена": float(product_price),
                    "количество": int(product_quantity), "ед": product_units}
    tuple_product = (prod_number, dict_product)

    return tuple_product


product_insert = create_product(len(goods_list) + 1)

while product_insert is not None:
    goods_list.append(product_insert)
    product_insert = create_product(len(goods_list) + 1)

list_prod_name = []
list_prod_price = []
list_prod_units = []
list_prod_quantity = []

if len(goods_list) > 0:
    for element in goods_list:
        list_prod_name.append(element[1].get("название"))
        list_prod_price.append(element[1].get("цена"))
        list_prod_quantity.append(element[1].get("количество"))
        list_prod_units.append(element[1].get("ед"))
    analytics = {"название": list_prod_name,
                 "цена": list_prod_price,
                 "количество": list_prod_quantity,
                 "ед": list_prod_units}
    for item in analytics.items():
        print(item)

else:
    print("В базе данных нет товаров!")

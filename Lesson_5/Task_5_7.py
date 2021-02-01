"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
 Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json


def positive_average(dict_firm):
    """Рассчёт средней прибыли, на входе словарь с инфо по фирмам"""
    average = 0
    num = 0
    for el in dict_firm:
        if dict_firm[el] > 0:
            num += 1
            average += dict_firm[el]

    return round((average / num), 2)


def firm_info(line):
    """формирование словаря - фирма: прибыль. на входе строка значений"""
    answer = {}
    firm = line.split(' ')
    firm_name = firm[0]
    income = float(firm[2])
    costs = float(firm[3]) if firm[3][:-1] != '\n' else float(firm[3][:-1])
    profit = income - costs
    answer[firm_name] = profit

    return answer


analytics = {}

with open('user_file_7.txt') as user_file:
    content = user_file.readlines()
    for element in content:
        analytics.update(firm_info(element))

dict_average_profit = {'average_profit': positive_average(analytics)}

answer_array = [analytics, dict_average_profit]

print(answer_array)

with open('analytics_firm_7.json', 'w') as json_file:
    json.dump(answer_array, json_file, ensure_ascii=False)

"""
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

list_data = ['Иванов 35000\n', 'Петров 15000\n', 'Сидоров 25000\n', 'Васичкин 10000\n']

with open('user_file_3.txt', 'w+') as user_file:
    user_file.writelines(list_data)
    user_file.seek(0)

    salary_sum = 0
    staff_salary_less_20 = []
    num_of_staff = 0

    for el in user_file:
        staff = el[:-1].split(' ')
        if float(staff[1]) < 20000:
            staff_salary_less_20.append(staff[0])
        salary_sum += float(staff[1])
        num_of_staff += 1

    print(f'Список сотрудников, чей заработок менее 20 тыс.: {staff_salary_less_20}')
    print(f'Средняя величина дохода сотрудников составляет: {salary_sum / num_of_staff}')

    #  Способ с построением словаря
    # staff_dict = {}
    #
    # for el in user_file:
    #     staff = el[:-1].split(' ')
    #     staff_surname = staff[0]
    #     staff_salary = float(staff[1])
    #     staff_dict[staff_surname] = staff_salary
    #
    # salary_20000 = [el for el in staff_dict if staff_dict[el] < 20000]
    # print(f'Список сотрудников, чей заработок менее 20 тыс.: {salary_20000}')
    #
    # salary_sum = 0
    # for num_of_staff, el in enumerate(staff_dict.values(), start=1):
    #     salary_sum += el
    #
    # print(f'Средняя величина дохода сотрудников составляет: {salary_sum / num_of_staff}')

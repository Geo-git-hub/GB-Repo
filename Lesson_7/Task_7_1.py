"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, *args):
        self.matrix = args
        self.dimension()

    def dimension(self):
        rows = 0
        columns = 0
        for el_row in self.matrix:
            rows = len(el_row)
            columns = len(el_row[0])
            for el in el_row[1:]:
                if len(el) == columns:
                    columns = len(el)
                else:
                    print(f'некорректная матрица, число столбцов в строках не совпадают {self.matrix}')

        return rows, columns

    def __str__(self):
        answer = ''
        for el_matrix in self.matrix:
            for el_row in el_matrix:
                answer += str(el_row) + '\n'
        return f'{answer}'

    def __add__(self, other):
        if self.dimension() != other.dimension():
            return f'у матриц разные размерности, операция сложение невозможна'
        else:
            new_matrix = []

            for i in range(len(self.matrix[0])):
                new_matrix_row = []
                for j in range(len(self.matrix[0][i])):
                    new_matrix_row.append(self.matrix[0][i][j] + other.matrix[0][i][j])
                new_matrix.append(new_matrix_row)

        return Matrix(new_matrix)


matrix_1 = Matrix([
    [31, 22],
    [37, 43],
    [51, 86]
])
print(matrix_1)
print('=============================================================')

matrix_2 = Matrix([
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64]
])

print(matrix_2)
print('=============================================================')

matrix_3 = Matrix([
    [3, 5],
    [8, 3],
    [7, 1]
])
print(matrix_3)
print('=============================================================')

matrix_4 = Matrix([
    [3, 5, 8],
    [8, 3, 6]
])
print(matrix_4)
print('=============================================================')

matrix_5 = matrix_1 + matrix_4
print(f'Сложение матриц 1 и 4: {matrix_5}')

matrix_6 = matrix_1 + matrix_3

print(f'Сложение матриц 1 и 3:\n{matrix_6}')

# print(f'{matrix_1 + matrix_3}')


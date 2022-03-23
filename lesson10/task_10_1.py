__author__ = 'Рейтер Валерия Борисовна'

# 1. Реализовать класс Matrix (матрица).
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
#
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# |  3  5 32 |
# |  2  4  6 |
#
# | -1 64 -8 |
# | 3 5 8 3 |
# | 8 3 7 1 |
#
# Формат вывода результата:
#
# Создать несколько матриц
# Вывести их с помощью print
# Выполнить сложение матриц и вывести результат сложения.
# Техническое задание:
#
# Данные в матрице хранятся как список списков целых чисел. Реализовать это через перегрузку конструктора.
# Реализовать перегрузку метода __str__() для вывода матрицы в привычном виде - как в примере. Выравнивание чисел
# не обязательно, но желательно. Метод __str__() возвращает строку.
# Реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица. Метод __add__() возвращает новую матрицу. Исходные матрицы остаются неизменными.
# Сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с первым
# том первой строки второй матрицы и пр.
# Подумайте о проверках корректности данных при создании матрицы и при их сложении
# Примеры/Тесты:
#
#
# >>> m1 = Matrix([[11,2,3],[4,5,6],[117,8,9]])
# >>> m2 = Matrix([[1,1,1],[1,1,1],[1,1,1]])
# >>> print(m1)
#
# |  11   2   3 |
# |   4   5   6 |
# | 117   8   9 |
#
# >>> print(m2)
#
# |   1   1   1 |
# |   1   1   1 |
# |   1   1   1 |
#
#
# >>> m4 = m1 + m2
# >>> print(m4)
#
# |  12   3   4 |
# |   5   6   7 |
# | 118   9  10 |
#
# >>> m3 = Matrix([[1,1],[1,1],[1,1]])
# >>> m5 = m1 + m3
# Traceback (most recent call last):
#   File "<interactive input>", line 1, in <module>
#   File "D:\\=WORK=\GEEKBRAINS\Python-I_files_\lesson-10\practical_task_solved\task_1.py", line 40,
#   in <span class="underline"><span class="underline">add</span></span>
#     raise ValueError("Incorrect dimensions for add method")
# ValueError: Incorrect dimensions for add method
# >>> m6 = Matrix([[1,1,1,1],[1,1,1],[1,1,1]])
# Traceback (most recent call last):
#   File "<interactive input>", line 1, in <module>
#   File "D:\\=WORK=\GEEKBRAINS\Python-I_files_\lesson-10\practical_task_solved\task_1.py", line 11,
#   in <span class="underline"><span class="underline">init</span></span>
#     raise ValueError("Incorrect data for Matrix initialization: not equal lenght of lists")
# ValueError: Incorrect data for Matrix initialization: not equal lenght of lists
# >>>


class Matrix:

    def __init__(self, lst_matr):
        if isinstance(lst_matr, list) and isinstance(lst_matr[0], list):
            self.lst_matr = list(lst_matr)
        else:
            raise ValueError("Объект Matrix должен быть списком списков")

    def __str__(self):
        lm = len(self.lst_matr)
        rez = ''
        for i in range(lm):
            for j in range(len(self.lst_matr[i])):
                if j == 0:
                    rez += '|'
                rez += "\t" + str(self.lst_matr[i][j])
                j += 1
            rez += "\t|\n"
            i += 1
        return rez

    def __add__(self, other):
        lm = len(self.lst_matr)
        if lm != len(other.lst_matr):
            raise ValueError("Размер складываемых матриц должен быть одинаковым")
        rez = []
        for i in range(lm):
            lm_i = len(self.lst_matr[i])
            rez_lst = []
            for j in range(lm_i):
                if lm_i != len(other.lst_matr[i]):
                    raise ValueError("Размер складываемых матриц должен быть одинаковым")
                rez_lst.append(self.lst_matr[i][j] + other.lst_matr[i][j])
                j += 1
                # print(rez_lst)
            rez.append(rez_lst)
            # print(rez)
            i += 1
        return Matrix(rez)


# m1 = Matrix([[11, 2, 3], [4, 5, 6], [117, 8, 9]])
# print(m1)
# b1 = Matrix('dsq')
# print(b1)


m1 = Matrix([[11, 2, 3], [4, 5, 6], [117, 8, 9]])
m2 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(m1+m2)

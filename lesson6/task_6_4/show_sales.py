__author__ = 'Рейтер Валерия Борисовна'

# Добавление записи
# Имя исполняемого скрипта: add_sale.py
# При записи передавать из командной строки значение суммы продаж. Функцию input не использовать.
# Новая запись дозаписывается в конец файла.
# Корректно обработать неправильное количество или тип переданных параметров.

from sys import argv
from os.path import join

count_arg = len(argv)

if count_arg > 3:
    print("Диапазон вывода данных можно указать максимально двумя аргументами")
elif count_arg > 1 and (not argv[1].isdigit() or not argv[2].isdigit()):
    print("Аргументы при вызове должны быть числовыми")
else:
    with open(file=join(".", "bakery.csv"), mode="rt", encoding='utf-8') as file_bak:
        for line in enumerate(file_bak):
            if (count_arg == 1 or (count_arg == 2 and line[0]+1 >= int(argv[1])) or
                    (count_arg == 3 and int(argv[1]) <= line[0]+1 <= int(argv[2]))):
                print(line[1].strip())



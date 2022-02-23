__author__ = 'Рейтер Валерия Борисовна'

# Добавление записи
# Имя исполняемого скрипта: add_sale.py
# При записи передавать из командной строки значение суммы продаж. Функцию input не использовать.
# Новая запись дозаписывается в конец файла.
# Корректно обработать неправильное количество или тип переданных параметров.

from sys import argv
from os.path import join

if len(argv) < 2 or len(argv) > 2:
    print("Необходимо ввести сумму одной продажи")
elif not argv[1].isdigit():
    print("Аргументы при вызове должны быть числовыми")
else:
    with open(file=join(".", "bakery.csv"), mode="at", encoding='utf-8') as file_bak:
        file_bak.write(argv[1]+'\n')

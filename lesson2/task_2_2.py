__author__ = 'Рейтер Валерия Борисовна'

# 2. Дан список строк. Выполнить обработку списка (смотри текст задания) и сформировать на его основе строку

first_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for elem in first_list:
    ind = first_list.index(elem)
    print(ind, elem)
    if isinstance(first_list[ind], int):
        first_list.insert(ind-1, '"')

print(first_list)


__author__ = 'Рейтер Валерия Борисовна'

# 2. Дан список строк. Выполнить обработку списка (смотри текст задания) и сформировать на его основе строку

# first_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
first_list = ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5', 'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']

i = 0
while i < len(first_list):
    if first_list[i][-1].isdigit():
        if len(first_list[i]) == 1:
            first_list[i] = '0' + first_list[i]
        elif first_list[i][0].isdigit() is False and len(first_list[i]) == 2:
            first_list[i] = first_list[i][0] + '0' + first_list[i][1]
        first_list.insert(i, '"')
        first_list.insert(i + 2, '"')
        i += 3
    else:
        i += 1
print(first_list)

first_str = first_list[0]
for i in range(1, len(first_list)):
    if first_str[-1].isdigit() is False and first_list[i][-1].isdigit() is False:
        first_str += ' '
    first_str += first_list[i]
print(first_str)

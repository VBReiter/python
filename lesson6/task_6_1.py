__author__ = 'Рейтер Валерия Борисовна'

# 1. Распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# Формат вывода результата:
#
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'HEAD', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_1'),
#     ...
# ]
#
# Техническое задание
#
# Не использовать библиотеки для парсинга. Только работа со строками.
# Создать список кортежей вида: `(<remote_addr>, <request_type>, <requested_resource>)`. Именно список кортежей.
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Вывести список на экран.
# Примечание:
#
# Файл логов можно загрузить отсюда:
# https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs
# В подобных структурированных файлах разделитель полей всегда очевиден.

from os.path import join

file_log = open(file=join(".", "nginx_logs.txt"), encoding="UTF-8", mode="rt")
result_ls = []
for line in file_log:
    remote_addr = line[0:line.find(' -')]
    request_type_start = line.find('"')
    request_type_end = line.find(' ', request_type_start)
    request_type = line[request_type_start+1:request_type_end]
    requested_resource = line[request_type_end+1:line.find(' ', request_type_end+1)]
    line_tl = (remote_addr, request_type, requested_resource)
    # print(line_tl)
    result_ls.append(line_tl)
print(result_ls)


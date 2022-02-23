__author__ = 'Рейтер Валерия Борисовна'

# 2. [Задача со звездочкой]: усложненный вариант задания 1. Найти IP адрес спамера и количество отправленных им
# запросов по данным файла логов из предыдущего задания. Спамер — это клиент, отправивший больше всех запросов.
# Формат вывода результата:
#
# Вывести IP спамера и количество запросов от него.
# Техническое задание
#
# Код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# У нас изначально нет никакой информации о максимальном количестве запросов. Его надо определить из лог-файла.
# Примечание:
#
# Не используйте затратные операций типа сортировки и поисков. Они здесь абсолютно избыточны. Для примера представьте,
# что более половина лог-файла - это запросы от спамера. Оцените эффективность вашего алгоритма в таком случае.
# Не используте сторонние модули для подсчетов, типа «count» - они вам не нужны.
# Уверены ли вы, что максимальное кол-во запросов - уникально? Т.е. найденный спамер - только один? Или таких спамеров
# может быть несколько?

# сначала создаем список по заданию 1
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
# print(result_ls)

# далее создаем словарь IP:кол-во запросов
dict_ip_requests = {}
for req in result_ls:
    request_ip = req[0]
    if request_ip in dict_ip_requests:
        dict_ip_requests[request_ip] += 1
    else:
        dict_ip_requests[request_ip] = 1

# вычисляем максимальное кол-во запросов и для него выводим IP
req_max = 0
for count_req in dict_ip_requests.values():
    if req_max < count_req:
        req_max = count_req

for request_ip, count in dict_ip_requests.items():
    if count == req_max:
        print(f"Максимательное количество запросов {req_max} было отправлено с адреса {request_ip}")

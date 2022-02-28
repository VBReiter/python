__author__ = 'Рейтер Валерия Борисовна'

# 5. [Задача со звездочкой]: усложненный вариант задания 4. Написать скрипт, который для заданной папки выводит
# статистику размеров файлов по расширениям.
# Формат вывода результата:
#
#
# {
#     100: [15, ['txt']],
#     1000: [3, ['py', 'txt']],
#     10000: [7, ['html', 'css']],
#     100000: [2, ['png', 'jpg']]
#   }
#
# Техническое задание
#
# Директорию с файлами some_data_adv можно скачать из прикрепленных к уроку файлов.
# Результат возвращается в виде словаря
# # ключи — верхняя граница размера файла (пусть будет кратна 10) - как в задании 4.
# значения — списки вида [<files_quantity>, [<files_extensions_list>]]. В список <files_extensions_list> заносятся все
# расширения для файлов удовлетворяющих условию размера, без повторений.
# Словарь сохраните в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

from os import scandir
from os.path import join

# stat_sublist = []
stat_dict = {100: [0], 1000: [0], 10000: [0], 100000: [0]}

start_folder = join(".", "task_7_4", "some_data_adv")
scan_folder = scandir(start_folder)
i_prev = 0
for item in scan_folder:
    if item.is_file():
        for i in stat_dict:
            stat_sublist = []
            if i_prev < item.stat().st_size < i:
                file_ext = item.name.rsplit(".")[1]
                # file_count = stat_dict[i][0] + 1
                stat_dict[i][0] += 1
                len_stat_dict = len(stat_dict[i])
                if len_stat_dict == 1 or file_ext not in stat_dict[i][1]:
                    if len_stat_dict > 1:
                        stat_sublist = stat_dict[i][1]
                    stat_sublist.append(file_ext)
                    if len_stat_dict > 1:
                        stat_dict[i][1] = stat_sublist
                    else:
                        stat_dict[i].append(stat_sublist)
            i_prev = i

print(stat_dict)

__author__ = 'Рейтер Валерия Борисовна'

# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
# |  |--settings
# |  |--mainapp
# |  |--adminapp
# |  |--authapp
#
# Техническое задание
#
# Продумайте ситуацию, когда все или часть этих папок уже есть в директории.
# Выберите наиболее подходящую структуру данных для хранения имен папок так, чтобы легко расширить количество
# создаваемых папок, например до 100 папок.
# Примечание:
# Можно ли будет расширять конфигурацию и хранить данные о вложенных папках и файлах?
from os import mkdir
from os.path import join, exists

structure = {"my project": ["settings", "mainapp", "adminapp", "authapp"]}

for key, val in structure.items():
    if not exists(join(".", key)):
        mkdir(join(".", key))
        for val_folder in val:
            if not exists(join(".", key, val_folder)):
                mkdir(join(".", key, val_folder))


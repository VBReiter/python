__author__ = 'Рейтер Валерия Борисовна'

# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates:
#
# |--my_project
# ...
# |--templates
# |   |--mainapp
# |   |  |--base.html
# |   |  |--index.html
# |   |--authapp
# |   |  |--base.html
# |   |  |--index.html
#
# Техническое задание
#
# В папках mainapp, authapp и аналогичных могут быть и другие файлы, кроме приведенных в примере.
# Папку templates надо создать внутри исходной директории, в примере - внутри my_project
# Шаблон - это папка templates в исходной структуре папок. Ее уровень в структуре папок может быть любым.
# Исходные файлы и папки необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён).
# Предусмотреть возможные исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.

from os import mkdir, walk, scandir
from os.path import join, exists, abspath
from shutil import copytree

templ_path = []
for root, dirs, files in walk(join(".", "my project")):
    if "templates" in root and "templates\\" not in root:
        templ_path.append(root)

# if not exists(join(".", "my project", "templates")):
#     mkdir(join(".", "my project", "templates"))

for t_folder in templ_path:
    scan_folder = scandir(t_folder)
    for item in scan_folder:
        try:
            copytree(join(".", t_folder, item.name), join(".", "my project", "templates", item.name))
        except FileExistsError:
            pass


# print(templ_path)




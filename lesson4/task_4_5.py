__author__ = 'Рейтер Валерия Борисовна'
# 5. [Задача со звездочкой]: Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.
# Используйте аргументы командной строки.
# Техническое задание
#
# Скрипт должен корректно обрабатывать только одну переданную ему валюту.
# Сделайте значимые сообщения пользователю о работе скрипта
# Скрипт могут запустить вообще без параметров, а могут с любым количеством параметров. Это надо учесть.
# Сделайте скриншот нескольких вызовов скрипта с разными аргументами.

from utils import currency_rates, currency_rates_advanced
from sys import argv

if len(argv) < 2:
    print("Необходимо ввести код валюты")
else:
    if len(argv) > 2:
        print("Возможен вывод курса только одной валюты")
    link = 'http://www.cbr.ru/scripts/XML_daily.asp'
    currency_code = argv[1]
    currency_rate = currency_rates(link, currency_code)
    if currency_rate is None:
        print("Не найдена валюта")
    else:
        print(f"Курс {currency_code.upper()}: {currency_rate}")

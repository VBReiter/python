__author__ = 'Рейтер Валерия Борисовна'

# 3. [Задача со звездочкой]: усложненный вариант задания 2. Доработать функцию currency_rates: теперь она должна
# возвращать курс валюты и дату, которая передаётся в ответе сервера. Название новой функции currency_rates_advanced.

from requests import get, utils
from datetime import date


def currency_rates_advanced(cur_link, cur_code):
    """Функция возвращает курс валюты cur_code и дату, на которую этот курс установлен, из источника cur_link"""
    response = get(cur_link)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    find_code = content.find(cur_code.upper())
    if find_code > 0:
        find_val = content.find('<Value>', find_code) + len('<Value>')
        end_val = content.find('</Value>', find_val)
        val = float(content[find_val:end_val].replace(",", "."))
    else:
        val = None
    find_date = content.find('ValCurs Date=') + len('ValCurs Date=')
    cur_date = map(int, reversed(str(content[find_date + 1:find_date + 11]).split(".")))
    (year, month, day) = cur_date
    return date(year, month, day), val


link = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency_code = 'qer'

print(currency_rates_advanced(link, currency_code))

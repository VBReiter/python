__author__ = 'Рейтер Валерия Борисовна'
# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, …)
# и возвращающую курс этой валюты по отношению к рублю.

from requests import get, utils
# from decimal import Decimal


def currency_rates(cur_link, cur_code):
    """Функция возвращает курс валюты cur_code из источника cur_link"""
    response = get(cur_link)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    find_code = content.find(cur_code.upper())
    if find_code > 0:
        find_val = content.find('<Value>', find_code) + len('<Value>')
        end_val = content.find('</Value>', find_val)
        val = float(content[find_val:end_val].replace(",", "."))
        # val = Decimal(float(content[find_val:end_val].replace(",", ".")))
        # val = val.quantize(Decimal("1.00"))
        return val
    else:
        return None


link = 'http://www.cbr.ru/scripts/XML_daily.asp'
currency_code = 'USD'

print(currency_rates(link, currency_code))



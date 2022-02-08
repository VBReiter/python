__author__ = 'Рейтер Валерия Борисовна'
# 1. Написать функцию num_translate, переводящую числительные от 0 до 10 c английского на русский язык.
# Если перевод сделать невозможно, вернуть объект None.


def num_translate(numb_eng, ls_numb):
    numb_eng = numb_eng.lower()
    if numb_eng in ls_numb:
        return ls_numb[numb_eng]
    else:
        return None


numbers = {
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
number = input('Input number: ')

print(num_translate(number, numbers))

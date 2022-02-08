__author__ = 'Рейтер Валерия Борисовна'

# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать функцию num_translate_adv, которая
# корректно обработает числительные, начинающиеся с заглавной буквы.
# Если перевод сделать невозможно, вернуть объект None.


def num_translate(number_eng, ls_numb):
    up = 0
    if number_eng[0].isupper():
        up = 1
    number_eng = number_eng.lower()
    if number_eng in ls_numb:
        number_rus = ls_numb[number_eng]
        if up == 1:
            number_rus = number_rus.capitalize()
        return number_rus
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

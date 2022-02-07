# 1. Написать функцию num_translate, переводящую числительные от 0 до 10 c английского на русский язык.
# Если перевод сделать невозможно, вернуть объект None.

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


def num_translate(number):
    number = number.lower()
    if number in numbers:
        return numbers[number]
    else:
        return None


number = input('Input number: ')
print(num_translate(number))

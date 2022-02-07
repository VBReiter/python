# 2. [Задача со звездочкой]: усложненный вариант задания 1. Написать функцию num_translate_adv, которая
# корректно обработает числительные, начинающиеся с заглавной буквы.
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


def num_translate(number, up):
    number = number.lower()
    if number in numbers:
        number_rus = numbers[number]
        if up == 1:
            print(number_rus[0])
            number_rus[0] = number_rus[0].upper()
        return number_rus
    else:
        return None


i = 0
number = input('Input number: ')
if number[0].isupper():
    i = 1
    print (number, i)
print(num_translate(number, i))

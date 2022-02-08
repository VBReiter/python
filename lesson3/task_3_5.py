__author__ = 'Рейтер Валерия Борисовна'

# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх заданных списков:
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

from random import choice


def get_jokes(quantity, ls_nouns, ls_adv, ls_adj):
    """Функция возвращает quantity-количество шуток, сформированных из трех случаных слов, взятых из трех списков:
        ls_nouns, ls_adv, ls_adj
    """
    i = 0
    jokes = []
    while i < quantity:
        jokes.append(f"{choice(ls_nouns)} {choice(ls_adv)} {choice(ls_adj)}")
        i += 1
    return jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(4, nouns, adverbs, adjectives))
print(get_jokes(quantity=4, ls_nouns=nouns, ls_adv=adverbs, ls_adj=adjectives))



__author__ = 'Рейтер Валерия Борисовна'

# 6. [Задача со звездочкой]: усложненный вариант задания 5.
# Добавьте в функцию еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках: каждое слово
# можно использовать только в одной шутке.
#
# Техническое задание
#
# Проверьте работу функции для разного количества шуток. Убедитесь в том, что каждое слово встречается только один раз.
# Примечание:
#
# Внимательно посмотрите какие из функций модуля random, упомянутые в методичке, подходят для реализации уникальности.
# Подумайте о том, сколько шуток можно вернуть при требовании уникальности, как это связано с размерами списков.
from random import choice
from random import sample


def get_jokes(quantity, ls_nouns, ls_adv, ls_adj, repeat=0):
    """Функция возвращает quantity-количество шуток, сформированных из трех случаных слов, взятых из трех списков:
        ls_nouns, ls_adv, ls_adj
        Параметр repeat разрешает или запрещает повторы слов в шутках: 0 - разрешены (по умолчанию), 1 - запрещены
    """
    i = 0
    jokes = []
    if repeat == 1:
        if len(ls_nouns) < quantity or len(ls_adv) < quantity or len(ls_adj) < quantity:
            return "Количество шуток больше количества слов в списках"
        else:
            ls_nouns_r = sample(ls_nouns, quantity)
            ls_adv_r = sample(ls_adv, quantity)
            ls_adj_r = sample(ls_adj, quantity)
            while i < quantity:
                joke_nouns = choice(ls_nouns_r)
                ls_nouns_r.remove(joke_nouns)
                joke_adv = choice(ls_adv_r)
                ls_adv_r.remove(joke_adv)
                joke_adj = choice(ls_adj_r)
                ls_adj_r.remove(joke_adj)
                jokes.append(f"{joke_nouns} {joke_adv} {joke_adj}")
                i += 1
    else:
        while i < quantity:
            jokes.append(f"{choice(ls_nouns)} {choice(ls_adv)} {choice(ls_adj)}")
            i += 1
    return jokes


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
print(get_jokes(6, nouns, adverbs, adjectives, 0))
print(get_jokes(quantity=6, ls_nouns=nouns, ls_adv=adverbs, ls_adj=adjectives, repeat=1))


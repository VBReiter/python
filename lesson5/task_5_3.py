__author__ = 'Рейтер Валерия Борисовна'

# 3. Есть два списка: tutors - имена учеников, groups - названия их классов. Необходимо реализовать генератор
# или функцию-генератор, возвращающий кортежи вида `(<tutor>, <group>)`.

# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def gen_group_tutor(tutors, groups):
    for i in range(len(tutors)):
        tut = tutors[i]
        if i >= len(groups):
            gr = None
        else:
            gr = groups[i]
        yield tut, gr


tutors_lst = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
groups_lst = ['9А', '7В', '9Б', '9В']
gen_end = gen_group_tutor(tutors_lst, groups_lst)

# while True:
#     next(gen_end)

while True:
    i = next(gen_end)
    print(i)

# for i in gen_end:
#     print(i)
# print(next(gen_end))

__author__ = 'Рейтер Валерия Борисовна'

# 3. Написать декоратор для логирования(вывод в консоль) типов позиционных аргументов функции:
# Примеры/Тесты:

# def type_logger...
#     ...
#
# @type_logger
# def render_input(*args, **kwargs):
#    return 1
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# Call for: calc_cube
# 5: <class 'int'>
# Rezult: 125  type: <class 'int'>
#
# >>> render_input(1, a = 2, b = True, c = "q")
# Call for: render_input
# 1: <class 'int'>
# 'a' = 2: <class 'int'>, 'b' = True: <class 'bool'>, 'c' = q: <class 'str'>
# Rezult: 1  type: <class 'int'>
#
# Техническое задание:
#
# Если аргументов несколько - выводить данные о каждом через запятую.
# Все выводы должны быть внутри функции-обертки(декораторе)
# После того как вы «обернули»/«задекорировали» функцию убедитесь что и аргументы, и возвращаемое значение остались
# как у исходной функции.
# Усложнение:
#
# вывести тип возвращаемого значения функции
# решить задачу для именованных аргументов
# вывести имя функции


def type_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Call for: {func.__name__}")
        arg_itog = ''
        kwarg_itog = ''
        for arg in args:
            arg_itog += f"{arg}: {type(arg)}, "
        for key, value in kwargs.items():
            kwarg_itog += f"{key} = {value}: {type(value)}, "
        if len(arg_itog) > 0:
            print(arg_itog.rstrip(', '))
        if len(kwarg_itog) > 0:
            print(kwarg_itog.rstrip(', '))
        result = func(*args, **kwargs)
        return f"Rezult: {result} {type(result)}\n"
    return wrapper


@type_logger
def render_input(*args, **kwargs):
    return 1


@type_logger
def calc_cube(x):
    return x ** 3


print(render_input(1, a=2, b=True, c="q"))
print(calc_cube(5))

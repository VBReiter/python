__author__='Рейтер Валерия Борисовна'

# Упрощенная версия скрипта
# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
# Формат вывода результата:
#
# до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сек.


duration = int(input('Введите длительность в секундах: '))
seconds = duration % 60
minutes = (duration // 60) % 60
hours = (duration // 3600) % 24
days = duration // (3600*24)

result = str(seconds)+' сек '
if minutes > 0:
    result = str(minutes)+' мин '+result
if hours > 0:
    result = str(hours) + ' час ' + result
if days > 0:
    result = str(days) + ' дн ' + result

print(result)

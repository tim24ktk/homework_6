from math import prod

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
#
# https://github.com/tim24ktk/homework_2/blob/main/task_4.py


value = int(input('Введите число больше нуля: '))

if value > 0:
    file = open('file.txt')
    indexes = file.read().split('\n')
    file.close()

    result = [i for i in range(-value, value + 1)]
    values = [result[int(i)] for i in indexes if i.isnumeric() and int(i) < len(result)]

    if len(indexes) == len(values):
        product = prod(values)

        print(f'Список из N элементов, заполненных числами из промежутка [-N, N]: {result}')
        print(f'Индексы из файла: {indexes}')
        print(f'Список элементов на указанных позициях: {values}')
        print(f'Произведение элементов на позициях указанных в файле: {product}')
    else:
        print(
            'Не удалось посчитать, т.к. один из индексов в файле больше чем длина списка или индекс указан не цифрами!')
else:
    print('Вы ввели неверное число!')

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]
# https://github.com/tim24ktk/homework_2/blob/main/task_3.py


def is_number(value: str) -> bool:
    """
    функция проверяет ли можно привести строку к вещественному числу,
    если нет то выбрасывает исключение
    :param value:
    :return:
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


number = input('Введите целое положительное число: ')

if is_number(number) and int(number) > 0:
    result = list(map(lambda i: (1 + 1 / i) ** i, range(1, int(number))))
    lst_sum = sum(result)

    print(f'Список из {number} чисел последовательности (1+1/n)^n: {result}')
    print(f'Их сумма равна: {lst_sum}')
else:
    print('Вы ввели неверное число!')
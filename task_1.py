
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# https://github.com/tim24ktk/homework_2/blob/main/task_1.py

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


def create_list(line: str) -> list:
    """
    создает список из цифр вещественного числа
    :param line: string
    :return: list
    """
    exceptions = ['.', '-']

    return [int(value) for key, value in enumerate(line) if value not in exceptions]


while True:
    number = input('Введите вещественное число: ')
    if is_number(number):
        print(sum(create_list(number)))
        break
    else:
        print('Вы ввели неверное значение! Попробуйте снова!')

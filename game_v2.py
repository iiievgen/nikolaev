"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def smart_predict(number: int = 1) -> int:
    """Угадываем число методом бинарного поиска.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    low = 1
    high = 100

    while low <= high:
        count += 1
        mid = (low + high) // 2
        if mid < number:
            low = mid + 1
        elif mid > number:
            high = mid - 1
        else:
            break  # Число найдено
    return count


def score_game(predict_func) -> int:
    """Оценка среднего количества попыток за 1000 подходов.

    Args:
        predict_func (function): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
# Генерируем массив из 1000 случайных чисел в диапазоне от 1 до 100
# Это наши "загаданные" числа для тестирования алгоритма
    random_array = np.random.randint(1, 101, size=1000) # загадали список чисел
# Для каждого числа из массива вызываем функцию угадывания 
# и сохраняем количество попыток в список count_ls
    count_ls = [predict_func(num) for num in random_array]
# Вычисляем среднее арифметическое значений списка попыток 
# и округляем до целого числа для наглядности
    score = int(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    # RUN 
    score_game(smart_predict)
  
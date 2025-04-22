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
            break
    return count

def score_game(predict_func) -> int:
    """Оценка среднего количества попыток за 1000 подходов.

    Args:
        predict_func (function): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    # np.random.seed(1)  # Раскомментируйте для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000)
    count_ls = [predict_func(num) for num in random_array]
    score = int(np.mean(count_ls))  # Исправлено nm -> np
    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    score_game(smart_predict)
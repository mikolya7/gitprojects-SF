import numpy as np


def game_core_v2(number, from_value=1, to_value=100):
    """ Угадываем число number в диапазоне (from_value, max_value) включительно,
        используем бинарный поиск
        возвращаем количество попыток, за которые угадали число.
    """
    found = False
    predictions_count = 0
    min_value = from_value
    max_value = to_value
    # в цикле угадываем число, каждый раз после удагывания сужаем диапазон
    # до тех пор, пока не угадали
    while not found:
        # пытаемся угадать number бинарным поиском
        predict = (min_value + max_value) // 2
        predictions_count += 1

        # если не угадали, то сужаем диапазон поиска
        if number > predict:
            min_value = predict + 1
        elif number < predict:
            max_value = predict - 1
        else:
            found = True  # угадали число number и завершаем цилк

    return predictions_count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# Проверяем
score_game(game_core_v2)

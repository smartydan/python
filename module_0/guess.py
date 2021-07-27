import numpy as np

def game_core(number):
    """Создаём левую и правую границу, каждый раз изменяя одну из них в соответствии
    с новой инфомацией(меньше или больше число), затем делим отрезок пополам"""
    count = 0
    left = 1
    right = 100
    predict = (left + right) // 2
    while True:
        count += 1
        if number == predict:
            return count
        elif number > predict:
            left = predict + 1
            predict = (left + right) // 2
        else:
            right = predict - 1
            predict = (left + right) // 2

def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return


score_game(game_core)
import numpy as np

def game_core_v2(number): # мы предположили число
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
    Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,101) #комп загадал число
    print('загаданное число', predict) # загаданное число
    while number != predict: #пока наше предположение не станет равно загаданному числу
        count+=1 # включаем счетчик попыток угадать
        if number < predict: # если предположенное число меньше загаданного, то
            number +=1 # прибавляем к предположенному числу единицу до загаданного числа
            print (number)
        elif number > predict: 
            number -= 1 # отнимаем от предположенного числа единицу до загаданного числа
            print(number)
    return count # выход из цикла, если угадали


        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
        score = int(np.mean(count_ls))
        print('Ваш алгоритм угадывает число в среднем за {} попыток'.format(score))
        return score
    
score_game(game_core_v2)